"""
AI Business Analyst — a simple CLI tool that turns a business problem
into structured analysis using the Anthropic Claude API.
"""

import os
import sys

from anthropic import Anthropic
from dotenv import load_dotenv

# Load API key from a .env file in this folder
load_dotenv()

MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5")

ANALYSIS_SECTIONS = [
    "Problem Statement",
    "Stakeholders",
    "Functional Requirements",
    "Non-Functional Requirements",
    "Risks",
    "User Stories",
    "Acceptance Criteria",
]


def get_api_key() -> str:
    """Read the Anthropic API key from the environment."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY is not set.")
        print("Copy .env.example to .env and add your API key.")
        sys.exit(1)
    return api_key


def get_business_problem() -> str:
    """Ask the user to describe their business problem."""
    print("Describe your business problem below.")
    print("Press Enter twice when you are done.\n")

    lines = []
    while True:
        line = input()
        if line == "" and lines:
            break
        lines.append(line)

    problem = "\n".join(lines).strip()
    if not problem:
        print("No problem entered. Exiting.")
        sys.exit(1)

    return problem


def build_prompt(problem: str) -> str:
    """Create the instruction sent to Claude."""
    sections = "\n".join(f"- {section}" for section in ANALYSIS_SECTIONS)

    return f"""You are a senior business analyst helping a team understand a new initiative.

The user described this business problem:

\"\"\"
{problem}
\"\"\"

Produce a clear, practical analysis with exactly these sections:

{sections}

Guidelines:
- Use markdown headings (##) for each section.
- Be specific to the problem described — avoid generic filler.
- Functional requirements describe what the system must do.
- Non-functional requirements cover performance, security, usability, etc.
- Write user stories in the format: "As a [role], I want [goal], so that [benefit]."
- Acceptance criteria should be testable and measurable where possible.
"""


def analyze_problem(client: Anthropic, problem: str) -> str:
    """Send the problem to Claude and return the analysis."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": build_prompt(problem)}],
    )

    return response.content[0].text


def main() -> None:
    print("=" * 50)
    print("  AI Business Analyst")
    print("=" * 50)
    print()

    client = Anthropic(api_key=get_api_key())
    problem = get_business_problem()

    print("\nAnalyzing your problem with Claude...\n")
    print("-" * 50)

    try:
        analysis = analyze_problem(client, problem)
    except Exception as error:
        print(f"Error calling Claude API: {error}")
        sys.exit(1)

    print(analysis)
    print("-" * 50)
    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
