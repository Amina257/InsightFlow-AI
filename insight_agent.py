from services.ollama_service import generate_response


def insight_agent(question: str, analysis: str) -> str:
    """
    Insight Agent:
    Converts analytical findings into important
    business insights and recommendations.
    """

    prompt = f"""
You are a Business Insight Agent.

Review the analysis below and identify the most important
business insights.

ANALYSIS:
{analysis}

ORIGINAL QUESTION:
{question}

Instructions:
- Identify the most important findings.
- Highlight risks, opportunities, or patterns when supported by the analysis.
- Do not invent facts.
- Give practical business insights.
- Keep the response structured and concise.

BUSINESS INSIGHTS:
"""

    return generate_response(prompt)