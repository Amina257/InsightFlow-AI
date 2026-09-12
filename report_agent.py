from services.ollama_service import generate_response


def report_agent(question: str, insights: str) -> str:
    """
    Report Agent:
    Converts business insights into a clear
    management-style report.
    """

    prompt = f"""
You are a Business Report Generation Agent.

Create a concise professional business report based only
on the insights provided below.

INSIGHTS:
{insights}

ORIGINAL QUESTION:
{question}

Structure the report as:

1. Executive Summary
2. Key Findings
3. Business Insights
4. Recommendations

Rules:
- Use only information supported by the insights.
- Do not invent numbers or facts.
- Keep the report professional and easy to understand.

BUSINESS REPORT:
"""

    return generate_response(prompt)