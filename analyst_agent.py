from services.ollama_service import generate_response


def analyst_agent(question: str, context: str) -> str:
    """
    Analyst Agent:
    Analyzes retrieved information and produces
    useful business insights.
    """

    prompt = f"""
You are a Business Data Analyst Agent.

Analyze the information provided below and answer the user's question.

CONTEXT:
{context}

QUESTION:
{question}

Instructions:
- Identify important facts and patterns.
- Highlight useful insights.
- Do not invent information.
- If the information is insufficient, say so.
- Keep the analysis clear and structured.

ANALYSIS:
"""

    return generate_response(prompt)
