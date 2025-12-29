# 🍛 Delhi Street Food Guide - Kiro CLI Agent

> Your local friend for navigating Delhi's incredible street food scene

A specialized Kiro CLI agent that provides authentic, practical street food recommendations across Delhi using comprehensive local knowledge. Built for the Kiro CLI Challenge.

## 🎯 What This Agent Does

This agent acts as a knowledgeable Delhi local who helps you discover the best street food based on:
- ⏰ Time of day (some foods only available at specific times!)
- 💰 Your budget (from ₹30 samosas to ₹300 full meals)
- 🥗 Dietary preferences (veg/non-veg/vegan/Jain/gluten-free)
- 📍 Your location or preferred area
- 🌶️ Your spice tolerance
- 🎭 Your experience level (tourist vs local)

Unlike generic food apps, this agent knows:
- Which vendors to visit at what time
- Exact metro stations and routes
- Local tips that only Delhi residents know
- Seasonal specialties (like Daulat Ki Chaat in winter!)
- Hidden gems vs tourist traps
- Real-time crowd patterns and optimal visiting hours

## 🏗️ Architecture

### Built Using Kiro CLI Features:

```
delhi-street-food-guide/
│
├── .kiro/
│   ├── agents/
│   │   └── delhi_food_agent.yaml      # Custom agent configuration
│   ├── steering.md                     # Agent behavior guidelines
│   └── hooks.yaml                      # Smart automation hooks
│
├── product.md                          # Local knowledge source (30 dishes, 10 zones)
├── README.md
└── screenshots/
    ├── agent-setup.png
    ├── example-conversation-1.png
    ├── example-conversation-2.png
    └── example-conversation-3.png
```

### Key Features Demonstrated:

1. **Custom Agent** (`delhi_food_agent.yaml`): Specialized agent with local context
2. **Local Context Integration** (`product.md`): 30+ dishes, 10 zones, comprehensive data
3. **Agent Steering** (`steering.md`): Behavioral guidelines and best practices
4. **Smart Hooks** (`hooks.yaml`): Automated workflow triggers and quality checks
5. **CLI-First Design**: No backend API, no SDK - pure Kiro CLI power

## 🚀 Quick Start

### Prerequisites
- Kiro CLI installed (see installation below)
- Basic familiarity with terminal

### Installation

1. Install Kiro CLI:
```bash
curl -fsSL https://cli.kiro.dev/install | bash
```

2. Clone this repository:
```bash
git clone https://github.com/yourusername/delhi-street-food-guide.git
cd delhi-street-food-guide
```

3. Initialize Kiro (if not already done):
```bash
kiro-cli
```

4. Run the agent:
```bash
cd /Users/srijansahu/Downloads/delhi-street-food-guide && streamlit run app_enhanced.py

Alternatively if you want to run on CLI then run below command:
kiro-cli chat --agent delhi-street-food-guide
```

## 💬 Example Conversations

### Example 1: Budget-Conscious Tourist
```
User: I'm near Rajiv Chowk at 6 PM, vegetarian, budget ₹80

Agent: Perfect timing for evening chaat! Head to Prince Paan Corner right in CP 
(2 min walk from Rajiv Chowk metro). Get their famous Gol Gappe (₹40-50) - 
crispy puris with that perfect chatpata paani that Delhi is famous for. 
Still have budget left? Add Papri Chaat (₹50-70) for the full experience.

Local tip: CP is clean and safe for first-timers. The vendors here use 
filtered water, so it's tourist-friendly. Peak crowd is 6-8 PM, so you're 
right on time!
```

### Example 2: Late Night Food Hunt
```
User: Late night non-veg food near Jama Masjid

Agent: Jama Masjid after 8 PM is magical for meat lovers! Head to Aslam Chicken 
(Jama Masjid metro, Violet Line) for their legendary Butter Chicken (₹150-200). 
Or try Karim's for authentic Seekh Kebabs (₹100-200) - they've been serving 
since 1913!

Both are open till 11 PM-midnight. The area gets super crowded around 8-9 PM, 
so go closer to 10 PM for a calmer experience. Cash preferred, though Karim's 
takes cards now.
```

### Example 3: First-Timer Guidance
```
User: First time in Delhi, what should I try?

Agent: Welcome to Delhi! Start safe and delicious at Connaught Place. Try these 
three must-haves:

1. Chole Bhature - Spicy chickpeas with fluffy fried bread (₹60-100). 
   Best at Bengali Market in the morning.
2. Gol Gappe - Delhi's addictive snack (₹30-50) at Prince Paan Corner, CP.
3. Momos - Safe bet! Try Khan Chacha in Khan Market (₹80-120).

All three spots are metro-connected, clean, and tourist-friendly. Start 
here, then level up to Old Delhi once you're comfortable!
```

## 🎨 Agent Features

### Context-Aware Recommendations
- **Seasonal Awareness**: Knows Daulat Ki Chaat is only available Nov-Feb
- **Time-Based Filtering**: Different foods for breakfast, lunch, evening, late night
- **Weather Consideration**: Suggests hot items in monsoon, cool items in summer
- **Festival Specials**: Aware of Ramadan, Diwali, Holi food traditions

### Practical Intelligence
- **Metro-First Navigation**: Always includes nearest metro station and line
- **Budget Optimization**: Respects your budget strictly, suggests alternatives
- **Crowd Management**: Warns about peak hours and suggests optimal visiting times
- **Safety First**: Honest about hygiene, crowds, and safety considerations

### Cultural Sensitivity
- **Dietary Respect**: Understands veg/non-veg/Jain/vegan/halal requirements
- **Local Terminology**: Uses Delhi slang naturally (Bhaiya, Tikha, Chatpata)
- **Experience Matching**: Adjusts recommendations based on user comfort level
- **Honest Warnings**: Upfront about spice levels, crowds, or challenges

## 📊 Knowledge Base

The agent draws from `product.md` which contains:
- **30 Street Food Items**: From ₹10 samosas to ₹300 tandoori chicken
- **10 Food Zones**: Chandni Chowk, CP, Karol Bagh, Majnu Ka Tila, etc.
- **Metro Integration**: Complete metro station mapping
- **Seasonal Items**: Winter specialties, summer coolers, festival foods
- **Local Tips**: Insider knowledge from years of Delhi street food experience
- **Price Ranges**: Accurate, up-to-date pricing for budget planning
- **Timing Details**: Exact hours when specific items are best

## 🔧 Technical Implementation

### Agent Configuration
The `delhi_food_agent.yaml` defines:
- Context source (product.md)
- Behavioral rules
- Response format requirements
- Example conversations for training
- Advanced capabilities

### Steering Guidelines
The `steering.md` provides:
- Interaction principles
- Tone guidelines
- Special scenario handling
- Quality control checks
- Cultural sensitivity rules

### Smart Hooks
The `hooks.yaml` implements:
- Pre-prompt context reminders
- Post-prompt quality verification
- Trigger-based responses (budget, first-time, spicy, etc.)
- Error handlers for edge cases
- Context enhancements

## 🎯 Why This Matters for Kiro CLI

This project demonstrates Kiro CLI's power to create:
1. **Domain-Specific Agents**: Not generic AI, but specialized local experts
2. **Context-Rich Intelligence**: Using local files as knowledge sources
3. **Automated Quality Control**: Hooks ensure consistent, reliable responses
4. **Practical Real-World Applications**: Solves actual user problems
5. **CLI-Native Workflows**: No backend, no API, just CLI + config

## 🤝 Contributing

While this is a Kiro CLI Challenge submission, suggestions for improving the knowledge base are welcome:
- New dishes or locations
- Updated prices or timings
- Better local tips
- Seasonal specialties

Please open an issue or PR with detailed information.

## 📜 License

MIT License - feel free to fork and adapt for your city!

## 🙏 Acknowledgments

- Built for the Kiro CLI Challenge
- Knowledge curated from years of Delhi street food exploration
- Inspired by the incredible food culture of Delhi
- Powered by Kiro CLI's agent framework

## 📸 Screenshots

See the `screenshots/` folder for:
- Agent setup and configuration
- Example conversations
- Different query patterns
- Response quality demonstrations

## 🔗 Links

- [Kiro CLI Documentation](https://docs.kiro.dev/)
- [Kiro CLI Challenge](https://docs.kiro.dev/challenge)
- [Delhi Metro Map](https://www.delhimetrorail.com/)

---

**Made with 🍛 for Delhi food lovers**

**For Kiro CLI Challenge | December 2024**