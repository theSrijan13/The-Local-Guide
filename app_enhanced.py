import streamlit as st
import subprocess
import json
import os
import tempfile
import re
from pathlib import Path

st.set_page_config(page_title="Delhi Street Food Guide", page_icon="🍛", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍛 Delhi Street Food Guide")
st.caption("Your local friend for navigating Delhi's incredible street food scene")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

def load_agent_config():
    """Load the agent configuration"""
    config_path = Path(".kiro/agents/delhi_food_agent.json")
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return None

def load_knowledge_base():
    """Load product.md knowledge base"""
    if Path("product.md").exists():
        with open("product.md") as f:
            return f.read()
    return ""

def clean_agent_output(output):
    """Clean ANSI escape codes and CLI formatting from agent output"""
    # Remove all ANSI escape sequences
    clean_output = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', output)
    clean_output = re.sub(r'\x1b\([AB]', '', clean_output)
    
    # Remove CLI formatting and headers
    clean_output = re.sub(r'╭[─┬╮]*╮.*?╰[─┴╯]*╯', '', clean_output, flags=re.DOTALL)
    clean_output = re.sub(r'Model:.*?\n', '', clean_output)
    clean_output = re.sub(r'Plan:.*?\n', '', clean_output)
    clean_output = re.sub(r'▸ Credits:.*?\n', '', clean_output)
    clean_output = re.sub(r'> ', '', clean_output)  # Remove prompt markers
    clean_output = re.sub(r'\[delhi-street-food-guide\].*?>', '', clean_output)  # Remove agent prompt
    
    # Clean up whitespace and empty lines
    lines = clean_output.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:  # Only keep non-empty lines
            cleaned_lines.append(line)
    
    response = '\n\n'.join(cleaned_lines) if cleaned_lines else ""
    return response

def call_kiro_agent(user_message):
    """Call Kiro CLI agent using subprocess"""
    try:
        # Call kiro-cli chat with the specific agent
        result = subprocess.run(
            ["kiro-cli", "chat", "--agent", "delhi-street-food-guide", "--no-interactive", user_message],
            capture_output=True,
            text=True,
            cwd=os.getcwd(),
            timeout=30
        )
        
        if result.returncode == 0:
            # Clean ANSI escape codes and CLI formatting
            response = clean_agent_output(result.stdout)
            return response if response else "I'm having trouble responding. Please try again."
        else:
            return f"⚠️ Agent error: {result.stderr[:200] if result.stderr else 'Unknown error'}"
            
    except subprocess.TimeoutExpired:
        return "⚠️ Request timed out. Please try a simpler query."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def process_query(query):
    """Process a query and add it to chat history"""
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Get agent response
    response = call_kiro_agent(query)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("🎯 Quick Filters")
    
    col1, col2 = st.columns(2)
    with col1:
        budget = st.number_input("Budget (₹)", 30, 1000, 150, step=50)
    with col2:
        time_of_day = st.selectbox("Time", ["Breakfast", "Lunch", "Evening", "Dinner", "Late Night"])
    
    dietary = st.selectbox("Dietary", ["Any", "Vegetarian", "Non-Vegetarian", "Vegan", "Jain", "Gluten-Free"])
    spice = st.select_slider("Spice Level", ["Mild", "Medium", "Spicy", "Very Spicy"])
    location = st.text_input("Location/Area", placeholder="e.g., Connaught Place")
    
    if st.button("🔍 Find Food", use_container_width=True, key="find_food_btn"):
        parts = []
        
        # Build query from filters
        if location:
            parts.append(f"near {location}")
        
        if dietary != "Any":
            parts.append(dietary.lower())
        
        parts.append(f"budget ₹{budget}")
        parts.append(f"{spice.lower()} spice")
        parts.append(f"for {time_of_day.lower()}")
        
        filter_prompt = f"Suggest street food {', '.join(parts)}"
        
        # Set pending query to process after rerun
        st.session_state.pending_query = filter_prompt
        st.rerun()
    
    st.divider()
    
    # Quick suggestions
    st.header("💡 Try These")
    suggestions = [
        "Best breakfast under ₹100",
        "Late night food near DU",
        "First time visitor recommendations",
        "Spicy non-veg in Old Delhi",
        "Vegan options in CP"
    ]
    
    for i, suggestion in enumerate(suggestions):
        if st.button(suggestion, key=f"sug_{i}", use_container_width=True):
            st.session_state.pending_query = suggestion
            st.rerun()
    
    st.divider()
    
    # Agent status
    st.header("🤖 Agent Status")
    agent_config = load_agent_config()
    if agent_config:
        st.success("✅ Agent Loaded")
        st.caption(f"Model: {agent_config.get('model', 'N/A')}")
    else:
        st.warning("⚠️ Agent config not found")
    
    try:
        result = subprocess.run(["kiro-cli", "--version"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            st.success("✅ Kiro CLI Ready")
        else:
            st.error("❌ Kiro CLI Error")
    except:
        st.error("❌ Kiro CLI Not Found")
    
    st.divider()
    
    if st.button("🗑️ Clear Chat", use_container_width=True, key="clear_chat_btn"):
        st.session_state.messages = []
        st.session_state.pending_query = None
        st.rerun()
    
    st.caption("Built with Kiro CLI • Delhi Street Food Guide")

# Process pending query if exists
if st.session_state.pending_query:
    query = st.session_state.pending_query
    st.session_state.pending_query = None  # Clear it
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Get agent response
    with st.spinner("🔍 Finding the best food for you..."):
        response = call_kiro_agent(query)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Force rerun to display the new messages
    st.rerun()

# Main chat area
if len(st.session_state.messages) == 0:
    # Welcome message
    st.info("""
    👋 **Welcome!** I'm your Delhi street food guide. Ask me about:
    - Specific dishes or locations
    - Budget-friendly options
    - Dietary restrictions
    - Best times to visit
    - Metro directions
    
    Or use the filters in the sidebar to get started!
    """)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about Delhi street food..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("🔍 Finding the best food for you..."):
            response = call_kiro_agent(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})