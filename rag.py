from retriever import search_documents


def build_context(query):
    results = search_documents(query)

    context = "\n\n".join(results)

    return context


def create_prompt(query):
    context = build_context(query)

    prompt = f"""
You are an AI Business Intelligence Analyst.

Use the following retrieved documents to answer the user's question.

CONTEXT:
{context}

QUESTION:
{query}

Instructions:
- Answer only using the provided context.
- If the answer is not available in the context, say "Information not found in the uploaded documents."
- Keep the answer clear and concise.

ANSWER:
"""

    return prompt