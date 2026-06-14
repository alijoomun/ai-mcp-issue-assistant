# AI MCP Issue Assistant

## Overview

`ai-mcp-issue-assistant` is a practical AI application that converts a rough business requirement into a structured GitHub-ready issue.

The project demonstrates how to combine:

- A simple Streamlit web application
- Google Gemini API as the LLM provider
- A local MCP server concept
- Secure API key management using environment variables
- GitHub workflow for version control and collaboration

The application is designed as a learning project for understanding how AI apps can use an LLM to generate useful business outputs and how MCP can be introduced as a tool layer.

---

## What the Application Does

The user enters a rough requirement into the Streamlit interface.

The application then sends the requirement to Google Gemini and asks the model to generate a structured GitHub issue containing:

- Summary
- User Story
- Acceptance Criteria
- Test Cases
- Open Questions
- Risks

The final result can be displayed in the app and downloaded as a Markdown file.

---

## High-Level Flow

```text
User
  |
  v
Streamlit Application
  |
  v
Application reads GEMINI_API_KEY from PC environment variables
  |
  v
Google Gemini API generates structured issue content
  |
  v
Local MCP server provides a reusable formatting tool concept
  |
  v
Final GitHub-ready issue is displayed to the user
```

### File Responsibilities

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit user interface |
| `issue_formatter.py` | Handles the Gemini API call |
| `mcp_server.py` | Defines the local MCP formatting tool |
| `requirements.txt` | Python dependencies |
| `.env.example` | Documents the required environment variable |
| `.gitignore` | Prevents unnecessary or sensitive files from being committed |

---

## Google Gemini API Usage

This project uses the Google Gemini API to generate structured content from a rough requirement.

The application sends a prompt to Gemini asking it to behave like a Product Owner, Business Analyst, and QA assistant.

The model is instructed to return the output using the following structure:

```markdown
## Summary

## User Story

## Acceptance Criteria

## Test Cases

## Open Questions

## Risks
```

Example logic from `issue_formatter.py`:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)
```

The returned response is then displayed inside the Streamlit application.

---

## API Key Storage

The Gemini API key must not be written directly in the source code.

The application expects the key to be stored in a PC environment variable named:

```text
GEMINI_API_KEY
```

This keeps the API key outside the GitHub repository and reduces the risk of accidentally exposing it.

---

## Setting the Gemini API Key on Windows

### Check if the key already exists

Open PowerShell and run:

```powershell
echo $env:GEMINI_API_KEY
```

If the key is displayed, the environment variable is already available.

### Set the key permanently

Run the following command in PowerShell:

```powershell
setx GEMINI_API_KEY "your_api_key_here"
```

After running `setx`, close PowerShell and open it again.

Then check again:

```powershell
echo $env:GEMINI_API_KEY
```

---

## How the Application Reads the API Key

The application reads the API key directly from the operating system environment variables.

Example from `issue_formatter.py`:

```python
import os

from google import genai


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY was not found in your PC environment variables. "
            "Please create a Windows user or system environment variable named GEMINI_API_KEY."
        )

    return genai.Client(api_key=api_key)
```

No `.env` file is required for this project.

The `.env.example` file is only used as documentation to explain which environment variable is expected.

---

## Setup Instructions

### 1. Clone the repository

```powershell
git clone https://github.com/alijoomun/ai-mcp-issue-assistant.git
cd ai-mcp-issue-assistant
```

### 2. Create a Python virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Confirm the Gemini API key exists

```powershell
echo $env:GEMINI_API_KEY
```

### 5. Run the application

```powershell
streamlit run app.py
```

---

## Dependencies

The project uses the following Python packages:

```text
streamlit
google-genai
mcp
```

---

## Example Test Case

Use the following automobile-related requirement to test the application:

```text
A car rental company wants customers to be able to reserve a vehicle online. The customer should select a pickup location, return location, pickup date, return date, and car category. The system should check availability and confirm the reservation if a suitable vehicle is available.
```

Expected output should include:

- A clear summary of the car reservation feature
- A user story from the customer perspective
- Acceptance criteria using Given/When/Then format
- Functional test cases for successful and failed reservation scenarios
- Open questions for missing business rules
- Risks related to availability, booking conflicts, validation, and integration

---

## Security Notes

Do not commit API keys to GitHub.

Avoid placing real secrets in:

- Source code
- README files
- `.env.example`
- Git commit history

The real Gemini API key should only exist in the local machine environment variable:

```text
GEMINI_API_KEY
```

---

## Goal of the Project

The goal of this project is to provide a simple but practical learning example of how to build an AI-enabled application using:

- A real LLM API
- Secure API key handling
- A simple web interface
- A local MCP server concept
- GitHub-based project structure and workflow

This project can be used as a foundation for more advanced AI agent applications.
