# ai-mcp-issue-assistant
AI Practical Exercise 1


2-Hour Practical Course: Build an AI App with MCP + LLM + GitHub
Course outcome

By the end, you will build:

AI GitHub Issue Assistant

The app will:

Take a rough requirement from the user.
Send it to an LLM.
Let the LLM call an MCP server tool.
Generate a structured GitHub issue.
Optionally create the issue in GitHub through the GitHub MCP server.

MCP is useful because it standardizes how AI apps connect to external tools and data sources, instead of every app needing custom integrations. OpenAI’s Agents SDK supports connecting agents to MCP servers, and GitHub has an official MCP server that allows AI tools to interact with repositories, issues, pull requests, code, and workflows.

Final app idea
App name
AI Requirement to GitHub Issue Generator
Example input
The user should be able to upload an invoice and the system should validate whether the invoice is accepted or rejected.
Example output
## Summary
Allow users to upload an invoice and receive a validation result.

## User Story
As an insurance operator, I want to upload an invoice so that I can know whether it is valid, rejected, or requires manual review.

## Acceptance Criteria
- Given I am on the invoice upload screen
  When I upload a valid invoice
  Then the system should show the invoice as accepted

- Given I upload an invalid invoice
  When validation fails
  Then the system should show the rejection reason

## Test Cases
1. Upload valid invoice
2. Upload unsupported file type
3. Upload invoice with missing mandatory fields
4. Upload duplicate invoice

## Open Questions
- What file formats are allowed?
- What validation rules should be applied?
- Should rejected invoices be stored for audit?

Then the agent can use MCP to create a GitHub issue.
