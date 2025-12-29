# Running the Streamlit UI

## Installation

```bash
pip install -r requirements.txt
```

## Run the App

### Basic Version
```bash
streamlit run app.py
```

### Enhanced Version (Recommended)
```bash
streamlit run app_enhanced.py
```

The app will open in your browser at `http://localhost:8501`

## Features

### Basic App (`app.py`)
- 💬 Chat interface with Kiro CLI integration
- 🎚️ Quick filters for budget, dietary preferences, and spice level
- 📝 Chat history maintained during session
- ✅ Agent status indicator

### Enhanced App (`app_enhanced.py`)
- 🎨 Improved UI with better layout
- 💡 Quick suggestion buttons
- 🔍 Advanced filters (time of day, location)
- 🤖 Agent configuration display
- 📊 Better conversation context handling
- ⚡ Faster response processing

## How It Works

The Streamlit app integrates with Kiro CLI by:
1. Reading the agent configuration from `.kiro/agents/delhi_food_agent.json`
2. Calling `kiro-cli chat` with user prompts via subprocess
3. Maintaining conversation context across messages
4. Displaying responses in a chat interface

## Requirements

- Kiro CLI must be installed and accessible in PATH
- Agent configuration must exist in `.kiro/agents/`
- `product.md` knowledge base must be present

## Troubleshooting

**Agent not responding:**
- Ensure Kiro CLI is installed: `kiro-cli --version`
- Check agent config exists: `.kiro/agents/delhi_food_agent.json`
- Verify you're in the project directory

**Slow responses:**
- The agent processes the full knowledge base
- First query may take longer
- Consider using the enhanced version for better performance

