# 🧠 Agentic AI Assignments - ReadMe

Welcome to the **Agentic AI Assignments Repository**. This repository contains three distinct assignments based on the concepts of AI agents, tools, orchestration, and real-time decision-making using OpenAI-compatible tool agents. Each assignment showcases unique use-cases of Agentic AI in different domains.

---

## 📁 Assignment 1: AI Agents Setup with FastAPI + Gemini

**Folder Name**: `assignment_1`

### ✅ Objective:

To build an AI agent environment using FastAPI and Gemini API, demonstrating tool-based interactions using Python functions.

### 🛠️ Features:

* FastAPI backend setup
* Tool usage: Country Info (capital, language, population)
* Environment configured with `.env` for secure key management

### 🚀 Tools Used:

* Python 3.10+
* Gemini API (OpenRouter)
* FastAPI
* Langchain
* Uvicorn

### 📂 Files:

* `main.py` → FastAPI server
* `tools.py` → Tools for answering queries
* `.env` → Your Gemini API key storage (do not push to GitHub)

---

## 📁 Assignment 2: Chat Agent with Streamed Response

**Folder Name**: `assignment_2`

### ✅ Objective:

Create a conversational AI agent using LangChain’s streaming features. The user will interact with a chatbot that can answer streamed questions using async chunked input/output.

### 🧠 Highlights:

* Chat agent with streaming
* Uses OpenRouter Gemini-compatible model
* Function tools for clean modular architecture

### ⚙️ Tools:

* Langchain
* Langchain Community
* Async/Streaming Support
* OpenRouter API key setup

### 📂 Files:

* `agent_chat.py`
* `stream_utils.py`
* `tools_streaming.py`

---

## 📁 Assignment 3: Country Info Bot (Agent as Tool)

**Folder Name**: `assignment_3`

### ✅ Objective:

Build 3 agent tools that return the following for a country:

1. Capital
2. Language
3. Population

An **orchestrator agent** then takes the user input (country name) and fetches all three details using the tools.

### 🔧 Tools:

* Gemini API via OpenRouter
* LangChain
* LangChain Tools
* Agent Executor

### 📦 Structure:

```bash
assignment_3/
├── agent_1/           # Capital Agent
│   └── capital_tool.py
├── agent_2/           # Language Agent
│   └── language_tool.py
├── agent_3/           # Population Agent
│   └── population_tool.py
├── orchestrator.py    # Main entry for combining all tools
└── .env               # Contains your OpenRouter API key
```

---

## 🧪 Running the Projects

1. Clone the repo:

```bash
git clone <repo-url>
cd <assignment-folder>
```

2. Setup virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

5. Run:

```bash
python orchestrator.py  # or appropriate entry file
```

---

## 🔐 Notes

* Do not share or commit `.env` to GitHub
* Always install dependencies in a virtual environment
* Use `git add .` only after validating all files are safe

---

## 🙌 Author

Developed by **Ayesha Mughal** as part of the Agentic AI coursework.

---

## 📬 Contact

For queries, reach out via GitHub or your course platform.

---

## 🏁 Happy Hacking!
