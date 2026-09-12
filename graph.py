from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from retriever import search_documents
from agents.bi_agent import business_intelligence_agent
from agents.analyst_agent import analyst_agent
from agents.insight_agent import insight_agent
from agents.report_agent import report_agent


# ============================================================
# STATE
# ============================================================

class BIState(TypedDict):
    question: str
    context: str
    answer: str
    analysis: str
    insights: str
    report: str


# ============================================================
# RETRIEVE DOCUMENT
# ============================================================

def retrieve_node(state: BIState):

    question = state["question"]

    results = search_documents(
        question,
        k=3
    )

    context = "\n\n".join(results)

    return {
        "context": context
    }


# ============================================================
# BUSINESS INTELLIGENCE AGENT
# ============================================================

def bi_agent_node(state: BIState):

    question = state["question"]
    context = state["context"]

    answer = business_intelligence_agent(
        question,
        context
    )

    return {
        "answer": answer
    }


# ============================================================
# ANALYST AGENT
# ============================================================

def analyst_agent_node(state: BIState):

    question = state["question"]
    context = state["context"]

    analysis = analyst_agent(
        question,
        context
    )

    return {
        "analysis": analysis
    }


# ============================================================
# INSIGHT AGENT
# ============================================================

def insight_agent_node(state: BIState):

    question = state["question"]
    analysis = state["analysis"]

    insights = insight_agent(
        question,
        analysis
    )

    return {
        "insights": insights
    }


# ============================================================
# REPORT AGENT
# ============================================================

def report_agent_node(state: BIState):

    question = state["question"]
    insights = state["insights"]

    report = report_agent(
        question,
        insights
    )

    return {
        "report": report
    }


# ============================================================
# BUILD LANGGRAPH
# ============================================================

graph_builder = StateGraph(BIState)


graph_builder.add_node(
    "retrieve",
    retrieve_node
)

graph_builder.add_node(
    "bi_agent",
    bi_agent_node
)

graph_builder.add_node(
    "analyst_agent",
    analyst_agent_node
)

graph_builder.add_node(
    "insight_agent",
    insight_agent_node
)

graph_builder.add_node(
    "report_agent",
    report_agent_node
)


# ============================================================
# GRAPH FLOW
# ============================================================

graph_builder.add_edge(
    START,
    "retrieve"
)

graph_builder.add_edge(
    "retrieve",
    "bi_agent"
)

graph_builder.add_edge(
    "bi_agent",
    "analyst_agent"
)

graph_builder.add_edge(
    "analyst_agent",
    "insight_agent"
)

graph_builder.add_edge(
    "insight_agent",
    "report_agent"
)

graph_builder.add_edge(
    "report_agent",
    END
)


# ============================================================
# COMPILE GRAPH
# ============================================================

bi_graph = graph_builder.compile()