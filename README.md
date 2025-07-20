# 🧠 Agentic AI Assignments – OpenAI Agents

This repository contains **three individual Python assignments** built using the OpenAI Agents framework. Each assignment is an independent application of AI agents to solve a specific task such as product recommendation, mood analysis, or country info retrieval using tools.

---

## 📁 Assignment 1: Smart Store Agent

**File:** `product_suggester.py`

### 📌 Objective:
Create an AI agent that can **suggest a product** based on the user's problem or query.

### 🧠 Functionality:
- The agent receives a user's input like `"I have a headache"`.
- It **analyzes the user's need** and suggests a relevant product (e.g., a medicine).
- It also explains **why** that product is a good fit for the user's need.

### ✅ Example Output:
```bash
User: I have a headache.
Agent: I recommend "Panadol". It helps relieve headaches due to its paracetamol content, which reduces pain and fever.
```
### 📁 Assignment 2: Mood Analyzer with Handoff
File: mood_handoff.py

📌 Objective:
Create a multi-agent system that analyzes a user’s mood and, if needed, hands off the task to another agent.

🧠 Functionality:
Agent 1: Detects mood from user message (happy, sad, angry, etc.).

If mood is "sad" or "stressed", it triggers:

Agent 2: Suggests a mood-lifting activity (e.g., go for a walk, listen to music).

Uses Runner.run() for invoking both agents.

✅ Example Flow:

User: I'm feeling really down lately...
Agent 1: Detected mood - sad.
Agent 2: Suggestion - Take a short walk outside or talk to a friend you trust.

📁 Assignment 3: Country Info Bot using Tools
File: country_info_toolkit.py

📌 Objective:
Use OpenAI tool agents to fetch information about countries based on user input.

🧠 Functionality:
Tool 1: Returns the capital of a country.

Tool 2: Returns the official language.

Tool 3: Returns the population.

An Orchestrator Agent takes the user's country name and calls all 3 tools using tool_choice and tool_output.

✅ Example Output:

User: Tell me about France.
Agent:
- Capital: Paris
- Language: French
- Population: 67 million
📦 Tech Stack
Python 🐍

OpenAI Agents SDK

JSON-based tool creation

CLI or terminal-based interaction

✅ How to Run
Install dependencies:


pip install -r requirements.txt
Set your OpenAI API key:


export OPENAI_API_KEY="your-key-here"
Run any assignment:


python product_suggester.py
python mood_handoff.py
python country_info_toolkit.py
📄 License
This project is for educational use under MIT License.

✨ Author
Made with ❤️ by Ayesha Mughal
For Agentic AI Quiz Practice – July 2025
