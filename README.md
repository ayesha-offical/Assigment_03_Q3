# 🧠 Agentic AI Assignments

This repository contains three interactive Python-based assignments demonstrating the use of AI agents using OpenAI's `openai-agents` SDK.

---

## 📁 Assignment 1: Smart Store Agent

**Filename:** `product_suggester.py`

### Objective:
Create an agent that suggests a product (medicine) based on user input.

### Functionality:
- If the user says "I have a headache", it should suggest a medicine (e.g., Paracetamol).
- The agent should also **explain the reason** for the suggestion.

---

## 📁 Assignment 2: Mood Analyzer with Handoff

**Filename:** `mood_handoff.py`

### Objective:
Detect mood and recommend activities.

### Functionality:
- **Agent 1** analyzes the mood from user message (like “happy”, “sad”, “stressed”).
- If mood is “sad” or “stressed”, a **handoff** to **Agent 2** occurs.
- **Agent 2** then suggests a mood-boosting activity (e.g., walk, meditation).
- Uses `Runner.run()` to invoke both agents.

---

## 📁 Assignment 3: Country Info Bot using Tools

**Filename:** `country_info_toolkit.py`

### Objective:
Build a country information retriever with tools.

### Functionality:
- Create **3 tool agents**:
  1. **Capital Finder**
  2. **Language Finder**
  3. **Population Finder**
- One **orchestrator agent** receives a country name and invokes all three tools.
- Returns structured information with capital, language, and population.

---

## ✅ Notes:
- All assignments are implemented in separate Python files.
- Agents utilize `OpenAI-Agent` interface via `Runner.run()` and `ToolAgent`.

---

## 🚀 Run Instructions:

```bash
pip install openai-agents
python product_suggester.py
python mood_handoff.py
python country_info_toolkit.py
```

## Author: 
**Made by Ayesha Faisal😊**
