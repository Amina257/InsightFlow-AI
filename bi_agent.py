from services.ollama_service import generate_response


def business_intelligence_agent(
    question: str,
    context: str
) -> str:

    prompt = f"""
You are an AI Business Intelligence Analyst.

Use ONLY the retrieved document context to answer
the user's question.

RETRIEVED CONTEXT:
{context}

USER QUESTION:
{question}

RULES:
1. Use only the information from the retrieved context.
2. Do not invent facts, numbers, names, skills, or statistics.
3. If the answer is not available in the context, say:
   "Information not found in the uploaded document."
4. Give a clear and direct answer.
5. Use bullet points when useful.

ANSWER:
"""

    return generate_response(prompt)