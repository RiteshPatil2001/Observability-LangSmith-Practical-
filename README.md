# 🔍 Observability with LangSmith — Practical Guide

A hands-on collection of AI applications built with **LangChain**, **LangGraph**, **RAG** and **Agents**, each fully instrumented with **LangSmith** for observability. Run any app and watch its traces, runs and agent activity appear live in your LangSmith dashboard.

---

## 📖 About the Project

This repository demonstrates how to implement **observability** for LLM-powered applications using **LangSmith**. It contains multiple independent AI applications covering the most common patterns in modern GenAI development:

- **LangChain** chains
- **LangGraph** workflows
- **RAG** (Retrieval-Augmented Generation) pipelines
- **AI Agents** with tool use

Every file in this repo is a **separate, standalone AI application**. Each one has its own `LANGSMITH_AGENT_ID` set explicitly in the code, so LangSmith creates a **separate agent for each application** and stores that application's traces only under its own agent. This keeps your dashboard clean and makes it easy to compare, debug and monitor each app individually.

---

## 🎯 What You'll Learn

- How to enable LangSmith tracing in LangChain / LangGraph applications
- How to separate traces per application using `LANGSMITH_AGENT_ID`
- How to inspect agent executions, traces and individual runs
- How to debug LLM calls, tool calls, retrieval steps and graph nodes
- How RAG pipelines and agents behave under the hood

---

## 🛠 Tech Stack

| Component | Purpose |
|-----------|---------|
| **LangChain** | Building LLM chains, prompts and tools |
| **LangGraph** | Building stateful, graph-based workflows and agents |
| **LangSmith** | Observability: tracing, monitoring and debugging |
| **Groq** | Fast LLM inference |
| **Hugging Face** | Embedding models / model access |
| **Tavily Search** | Web search tool for agents |
| **Python** | Core language |

---

## 📂 Project Structure

```
Observability-LangSmith-Practical-/
│
├── <application_1>.py      # Standalone AI app (description at top of file)
├── <application_2>.py      # Standalone AI app (description at top of file)
├── <application_3>.py      # Standalone AI app (description at top of file)
├── ...
├── <theory>.pdf            # Theory document on observability / LangSmith
├── requirements.txt        # Python dependencies
├── .env                    # Your API keys (you create this, not committed)
└── README.md
```

> 💡 **Tip:** Each application file begins with a comment block explaining **what the application is**, **what it does**, and its **use case**. Read that block first before running a file.

---

## ✅ Prerequisites

- **Python 3.10 or higher** — [Download Python](https://www.python.org/downloads/)
- **Git** — [Download Git](https://git-scm.com/downloads)
- Free accounts on Groq, Hugging Face, LangSmith and Tavily (steps below)

---

## 🔑 Step 1: Get Your API Keys

You need four API keys. All of them have free tiers.

### 1️⃣ Groq API Key

1. Go to the [Groq Console](https://console.groq.com/) and sign up or log in.
2. Open the [API Keys page](https://console.groq.com/keys).
3. Click **Create API Key**, give it a name, and click **Submit**.
4. **Copy the key immediately.** It is shown only once.

### 2️⃣ Hugging Face API Token

1. Go to [Hugging Face](https://huggingface.co/join) and sign up or log in.
2. Open [Settings → Access Tokens](https://huggingface.co/settings/tokens).
3. Click **Create new token**.
4. Choose the **Read** token type (enough for this project), give it a name, and click **Create token**.
5. Copy the token (it starts with `hf_`).

### 3️⃣ LangSmith API Key

1. Go to [LangSmith](https://smith.langchain.com/) and sign up or log in.
2. Click the **Settings** (gear) icon, or go directly to [LangSmith Settings](https://smith.langchain.com/settings).
3. Open the **API Keys** section and click **Create API Key**.
4. Choose a key type (**Personal Access Token** works well for local development), name it, and click **Create**.
5. Copy the key immediately. It is shown only once.

📚 Docs: [LangSmith Documentation](https://docs.smith.langchain.com/)

### 4️⃣ Tavily Search API Key

Used by the `TavilySearchResults` tool in the agent applications.

1. Go to [Tavily](https://app.tavily.com/) and sign up or log in.
2. After login, your **API key** is shown on the dashboard (it starts with `tvly-`).
3. Copy the key.

📚 Docs: [Tavily Documentation](https://docs.tavily.com/)

---

## 📥 Step 2: Clone the Repository

```bash
git clone https://github.com/RiteshPatil2001/Observability-LangSmith-Practical-.git
cd Observability-LangSmith-Practical-
```

---

## ⚙️ Step 3: Create the `.env` File

In the **root folder** of the project, create a file named `.env` and paste the following:

```env
GROQ_API_KEY=""
HUGGINGFACEHUB_API_TOKEN=""
TAVILY_API_KEY=""

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=""
LANGSMITH_AGENT_ID=""
LANGSMITH_AGENT_ENVIRONMENT="local"
```

Fill in each value with the keys you created in Step 1.

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key |
| `HUGGINGFACEHUB_API_TOKEN` | Your Hugging Face access token |
| `TAVILY_API_KEY` | Your Tavily search API key |
| `LANGSMITH_TRACING` | Set to `true` to enable tracing |
| `LANGSMITH_ENDPOINT` | LangSmith API URL. Use `https://api.smith.langchain.com` (default for US region) |
| `LANGCHAIN_API_KEY` | Your LangSmith API key |
| `LANGSMITH_AGENT_ID` | Agent name shown in LangSmith. Each app file sets its own explicitly, so a default here is optional |
| `LANGSMITH_AGENT_ENVIRONMENT` | Environment label, keep as `local` |

> ⚠️ **Never commit your `.env` file or share your API keys publicly.** Make sure `.env` is listed in your `.gitignore`.

---

## 🐍 Step 4: Create a Virtual Environment

**Windows (Command Prompt / PowerShell):**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

When activated, you'll see `(venv)` at the start of your terminal line.

---

## 📦 Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Step 6: Run the Applications

Each file in this repo is a **separate AI application**. Run any one on its own:

```bash
python <file_name>.py
```

For example:

```bash
python rag_app.py
python agent_app.py
```

### What to expect

- At the **top of every file** you'll find a description of the application: what it is, what it does, and its use case.
- Each file sets its own `LANGSMITH_AGENT_ID`, so LangSmith creates a **dedicated agent** for it.
- Every run is traced automatically and stored under that application's agent only.

---

## 📊 Viewing Traces in LangSmith

1. Log in to [LangSmith](https://smith.langchain.com/).
2. Open your workspace and go to **Tracing / Projects** to see your runs.
3. Open the **Agents** view to find a separate agent for each application you ran.
4. Click an agent to see its **executions, traces and runs**.
5. Open any trace to inspect:
   - LLM inputs and outputs
   - Tool calls (e.g. Tavily search)
   - Retrieval steps in RAG pipelines
   - LangGraph node-by-node execution
   - Latency, token usage and errors

---

## 📘 Theory PDF

This repo includes a **theory PDF** covering the concepts behind observability and LangSmith. Read it before or alongside running the applications to understand what you see in the traces.

---

## 🧰 Troubleshooting

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError` | Activate your virtual environment and re-run `pip install -r requirements.txt` |
| `Invalid API key` errors | Re-check the keys in `.env` and make sure there are no extra spaces or quotes problems |
| No traces in LangSmith | Confirm `LANGSMITH_TRACING=true` and that `LANGCHAIN_API_KEY` is valid |
| `.env` not loading | Make sure the file is named exactly `.env` and sits in the project root |
| PowerShell blocks venv activation | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again |

---

## 🤝 Contributing

Suggestions and improvements are welcome. Feel free to open an issue or submit a pull request.

## ⭐ Support

If this repo helped you, please give it a star on GitHub!

---

**Author:** [Ritesh Patil](https://github.com/RiteshPatil2001)
