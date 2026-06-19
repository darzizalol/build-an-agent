from dotenv import load_dotenv
load_dotenv()

import os
import csv
import io

from langchain.agents import create_agent
from langchain_core.tools import tool
from pathlib import Path

skills_dir = Path(__file__).resolve().parent / "skills"
system_prompt = "\n\n".join(p.read_text() for p in sorted(skills_dir.rglob("*.md")))

rows = [
    ["Date", "Product", "Units", "Revenue"],
    ["2025-08-01", "Widget A", 10, 250],
    ["2025-08-02", "Widget B", 5, 125],
    ["2025-08-03", "Widget A", 7, 175],
    ["2025-08-04", "Widget C", 3, 90],
]

with open("sales.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

@tool
def read_file(path: str) -> str:
    """Read the contents of a local file by path."""
    with open(path, "r") as f:
        return f.read()

agent = create_agent("anthropic:claude-haiku-4-5", tools=[read_file], system_prompt=system_prompt)

stream = agent.stream_events(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Read sales.csv and summarize total revenue by product in one sentence."
                ),
            }
        ]
    },
    version="v3",
    config={"recursion_limit": 8},
)

for item in stream.messages:
    print(item.text)