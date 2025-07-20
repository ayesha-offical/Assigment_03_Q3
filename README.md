# 🧠 Agentic AI Assignments – Toolkit Series

This repository contains three assignments developed using **OpenAI's Agentic Framework with Tool usage**, focusing on practical implementations of agents and orchestrators using Python.

---

## 📁 Assignment 1: Simple Capital Info Agent

### 🔹 File: `main.py`

This is a basic agent using the **Function as a Tool** approach.

### ✅ Features:
- Takes a country name as input.
- Uses a function tool to return its capital.
- Responds through a chat loop.

### 💡 Sample Output:
User: What is the capital of France?
Agent: The capital of France is Paris.

---

## 📁 Assignment 2: Toolkit with Multiple Tools

### 🔹 File: `multi_toolkit.py`

This assignment extends the previous idea with **multiple tools** in a single toolkit agent.

### ✅ Tools Implemented:
- Get Capital
- Get Language
- Get Population

### 💡 Sample Output:
Country: Japan
Capital: Tokyo
Language: Japanese
Population: 126,000,000

markdown
---

## 📁 Assignment 3: Country Info Bot with Tool Agents

### 🔹 File: `country_info_toolkit.py`

This assignment builds a **multi-agent system**, where each tool is separated into its own agent. An **orchestrator agent** calls each of them as needed.

### 🧰 Agents Used:
1. `capital_agent`: Returns the capital of the country.
2. `language_agent`: Returns the official language(s).
3. `population_agent`: Returns the population.
4. `orchestrator_agent`: Coordinates all above agents to give full country info.

### 💡 Sample Output:
User: Tell me about Pakistan
Response:
Capital: Islamabad
Language: Urdu
Population: 241,000,000

---

## 🧪 Technologies Used
- Python 3.10+
- OpenAI Agents SDK
- dotenv
- Tool Abstractions via `tool()` decorator
- Agent-Orchestration Logic

---

## 📦 Setup Instructions

```bash
git clone https://github.com/your-username/agentic-assignments.git
cd agentic-assignments

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API Key
touch .env
echo "GEMINI_API_KEY=your_key_here" >> .env
🚀 Run Examples

# For Assignment 1
python main.py

# For Assignment 2
python multi_toolkit.py

# For Assignment 3
python country_info_toolkit.py
✍️ Author
👩‍💻 Ayesha Mughal
🚀 Passionate about Agentic AI | Pythonista | Frontend Developer
