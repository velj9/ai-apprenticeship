# AI Business Analyst

A beginner-friendly Python CLI that turns a plain-language business problem into structured analysis using the Anthropic Claude API.

## What it does

You describe a business problem. Claude returns:

- Problem Statement
- Stakeholders
- Functional Requirements
- Non-Functional Requirements
- Risks
- User Stories
- Acceptance Criteria

## Prerequisites

- Python 3.10 or newer
- An [Anthropic API key](https://console.anthropic.com/)

## Setup

1. Open a terminal in this folder:

   ```bash
   cd projects/ai-business-analyst
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

   Activate it:

   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy the example environment file and add your API key:

   ```bash
   copy .env.example .env
   ```

   Edit `.env` and replace `your_api_key_here` with your real key.

## Run

```bash
python app.py
```

Type your business problem, press Enter twice when finished, and wait for Claude's analysis.

### Example input

```
Our small retail shop tracks inventory in spreadsheets.
Staff often sell items that are already out of stock,
and managers spend hours each week updating stock counts manually.
```

## Project files

| File | Purpose |
|------|---------|
| `app.py` | Main application — collects input, calls Claude, prints results |
| `requirements.txt` | Python packages needed to run the app |
| `.env.example` | Template for your secret API key (copy to `.env`) |
| `README.md` | Setup and usage instructions |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ANTHROPIC_API_KEY is not set` | Create a `.env` file from `.env.example` and add your key |
| `Error calling Claude API` | Check your API key, internet connection, and account credits |
| Import errors | Activate your virtual environment and run `pip install -r requirements.txt` |
