# Build an Agent

A simple LangChain agent that reads a local CSV file and summarizes its contents using a language model.

## Setup

### 1. Clone the repo

```bash
git clone <repo-url>
cd build-an-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install langchain langchain-core python-dotenv
```

### 4. Configure environment variables

Copy the example env file and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your keys:

| Variable | Where to get it |
|---|---|
| `LANGSMITH_API_KEY` | [smith.langchain.com](https://smith.langchain.com) → Settings → API Keys |
| `LANGSMITH_TRACING` | Set to `true` to enable LangSmith tracing |
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) → API Keys |

### 5. Run the agent

```bash
python create_agent.py
```

The agent will generate `sales.csv`, read it using a file-reading tool, and print a one-sentence revenue summary by product.
