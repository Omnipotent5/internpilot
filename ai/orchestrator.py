from langgraph.graph import StateGraph, END
from typing import TypedDict
from ai.agents import (
    planner_agent,
    architect_agent,
    coder_agent,
    reviewer_agent,
    debugger_agent,
)

import os


class AgentState(TypedDict, total=False):
    task: str
    plan: str
    architecture: str
    code: str
    review: str
    fixed_code: str


graph = StateGraph(AgentState)

graph.add_node("planner", planner_agent)
graph.add_node("architect", architect_agent)
graph.add_node("coder", coder_agent)
graph.add_node("reviewer", reviewer_agent)
graph.add_node("debugger", debugger_agent)

graph.set_entry_point("planner")

graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.add_edge("coder", "reviewer")
graph.add_edge("reviewer", "debugger")
graph.add_edge("debugger", END)

app = graph.compile()


if __name__ == "__main__":

    task = input("Enter development task: ")

    result = app.invoke({"task": task}) or {}

    print("\n===== PLAN =====\n")
    print(result.get("plan", "No plan generated"))

    print("\n===== ARCHITECTURE =====\n")
    print(result.get("architecture", "No architecture generated"))

    print("\n===== CODE =====\n")
    print(result.get("fixed_code", "No code generated"))

    os.makedirs("generated", exist_ok=True)

    code = result.get("fixed_code")

    if code:
        with open("generated/output_code.py", "w", encoding="utf-8") as f:
            f.write(code)

        print("\nCode saved to generated/output_code.py")