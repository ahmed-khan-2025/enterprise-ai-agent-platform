from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.agents.investigation_agent import investigation_agent
from app.agents.decision_agent import decision_agent
from app.agents.response_agent import response_agent


def build_workflow():

    graph = StateGraph(AgentState)

    graph.add_node(
        "investigation",
        investigation_agent,
    )

    graph.add_node(
        "decision",
        decision_agent,
    )

    graph.add_node(
        "response",
        response_agent,
    )

    graph.add_edge(
        START,
        "investigation",
    )

    graph.add_edge(
        "investigation",
        "decision",
    )

    graph.add_edge(
        "decision",
        "response",
    )

    graph.add_edge(
        "response",
        END,
    )

    return graph.compile()