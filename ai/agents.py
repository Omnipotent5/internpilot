from langchain_ollama import ChatOllama

# reasoning model
planner_llm = ChatOllama(
    model="qwen2.5-coder:7b",
    temperature=0.2,
)

# coding model
coder_llm = ChatOllama(
    model="deepseek-coder:6.7b",
    temperature=0.1,
)


def planner_agent(state):
    task = state.get("task", "")

    prompt = f"""
You are a senior software planning expert.

Create a clear implementation plan for the following task.

Task:
{task}
"""

    response = planner_llm.invoke(prompt)
    state["plan"] = response.content
    return state


def architect_agent(state):
    plan = state.get("plan", "")

    prompt = f"""
You are a senior software architect.

Design a clean system architecture based on this implementation plan.

Plan:
{plan}
"""

    response = planner_llm.invoke(prompt)
    state["architecture"] = response.content
    return state


def coder_agent(state):
    architecture = state.get("architecture", "")

    prompt = f"""
You are a senior Python engineer.

Implement working Python code based on the architecture below.

Architecture:
{architecture}

Return complete code.
"""

    response = coder_llm.invoke(prompt)
    state["code"] = response.content
    return state


def reviewer_agent(state):
    code = state.get("code", "")

    prompt = f"""
You are a strict code reviewer.

Analyze the following code and list problems, bugs, and improvements.

Code:
{code}
"""

    response = planner_llm.invoke(prompt)
    state["review"] = response.content
    return state


def debugger_agent(state):
    code = state.get("code", "")
    review = state.get("review", "")

    prompt = f"""
You are a senior debugging expert.

Fix any problems in the code below using the review comments.

Original Code:
{code}

Review Comments:
{review}

Return the corrected version of the code.
"""

    response = planner_llm.invoke(prompt)
    state["fixed_code"] = response.content
    return state