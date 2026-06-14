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


def generate_issue_content(requirement: str) -> str:
    client = get_gemini_client()

    prompt = f"""
You are a senior Product Owner, Business Analyst, and QA assistant.

Convert the rough requirement below into a GitHub-ready issue.

Return the answer using exactly these headings:

## Summary
## User Story
## Acceptance Criteria
## Test Cases
## Open Questions
## Risks

Rules:
- Acceptance criteria must use Given/When/Then format.
- Test cases must be practical and numbered.
- Open questions must be useful for a Product Owner.
- Risks must include functional, testing, and integration risks.
- Keep the output concise but complete.

Requirement:
{requirement}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text