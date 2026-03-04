# CLAUDE.md

This file defines how Claude Code agents should operate when working in the **InternPilot** repository.

InternPilot is an AI-powered system that automatically discovers startups, analyzes job descriptions, personalizes resumes, generates cover letters, and manages internship applications.

The system uses a **multi-agent development workflow**, Antigravity skills, and local LLMs via Ollama.

---

# Project Overview

InternPilot is built using a modular full-stack architecture.

Primary technologies:

Backend
- Python
- FastAPI

Frontend
- Next.js
- React

Database
- Supabase / PostgreSQL

AI System
- Ollama local models
- Multi-agent architecture

The repository is structured to support **AI-assisted development using Claude Code agents**.

---

# Repository Structure

internpilot
│
├ agents
│ AI development agents (planner, architect, reviewer, etc.)
│
├ commands
│ Slash commands that trigger agents
│
├ skills
│ Antigravity skills used to enforce best practices
│
├ backend
│ FastAPI backend services
│
│ ├ api
│ ├ models
│ ├ services
│ └ agents
│
├ frontend
│ Next.js frontend application
│
│ ├ app
│ ├ components
│ └ lib
│
├ database
│ Database schema and migrations
│
├ ai
│ AI orchestration logic
│
├ hooks
│ Automation hooks triggered during agent workflows
│
└ CLAUDE.md


---

# AI Agent System

This repository uses multiple specialized agents.

Agents must follow clear responsibilities.

### Architect
Responsible for:

- system architecture
- database schema
- service boundaries
- API design

### Planner

Responsible for:

- breaking features into implementation plans
- identifying dependencies
- defining implementation order

### Code Reviewer

Responsible for:

- code quality
- architecture alignment
- maintainability

### Python Reviewer

Responsible for:

- reviewing Python code
- performance issues
- security issues

### Refactor Cleaner

Responsible for:

- improving code structure
- removing duplication
- improving readability

### Build Error Resolver

Responsible for:

- fixing runtime errors
- resolving build failures
- debugging issues

### TDD Guide

Responsible for:

- guiding test-driven development
- ensuring proper test coverage

---

# Agent Workflow

Typical workflow for implementing a feature:

---

# AI Agent System

This repository uses multiple specialized agents.

Agents must follow clear responsibilities.

### Architect
Responsible for:

- system architecture
- database schema
- service boundaries
- API design

### Planner

Responsible for:

- breaking features into implementation plans
- identifying dependencies
- defining implementation order

### Code Reviewer

Responsible for:

- code quality
- architecture alignment
- maintainability

### Python Reviewer

Responsible for:

- reviewing Python code
- performance issues
- security issues

### Refactor Cleaner

Responsible for:

- improving code structure
- removing duplication
- improving readability

### Build Error Resolver

Responsible for:

- fixing runtime errors
- resolving build failures
- debugging issues

### TDD Guide

Responsible for:

- guiding test-driven development
- ensuring proper test coverage

---

# Agent Workflow

Typical workflow for implementing a feature:
User request
↓
/plan
↓
Planner → Architect
↓
Implementation Plan
↓
User confirmation
↓
Code generation
↓
Code review
↓
Refactor
↓
Test


Commands should never skip the planning phase.

Agents must **never generate code without a plan first**.

---

Commands must **never skip the planning phase**.

Agents must **never generate code without a plan first**.

---

# Development Execution Loop

When implementing a feature Claude should follow this loop:

1. Analyze the user request
2. Use the **Planner agent** to generate a detailed plan
3. Use the **Architect agent** to validate system design
4. Delegate implementation to **Aider**
5. Review generated code
6. Fix issues if necessary
7. Confirm feature completion

Claude should repeat this loop until the feature is fully implemented.

---

# External Tools

Claude can delegate repository editing tasks to **Aider**.

Aider is responsible for modifying files inside the repository.

Claude must use the following command for implementation tasks:

python scripts/run_aider_task.py "<task description>"

Example:
python scripts/run_aider_task.py "Create SQLAlchemy models for users, companies, and applications"

Rules:

- Claude performs planning and architecture decisions
- Aider performs file edits
- Claude reviews the resulting code
- Claude may call Aider multiple times to refine the implementation

Claude should **not directly modify repository files** when Aider is available.

---

# Skill System

The repository uses **Antigravity skills** stored in `/skills`.

Agents must consult relevant skills before producing output.

Skill categories:

### Architecture Skills

- api-design-principles
- api-patterns
- database-design
- database-architect

---

### Backend Skills

- python-fastapi-development
- python-development-python-scaffold
- python-patterns
- api-security-best-practices
- api-documentation

---

### Frontend Skills

- react-nextjs-development
- react-best-practices
- react-ui-patterns
- react-state-management

---

### Code Quality Skills

- python-testing-patterns
- debugging-strategies
- code-reviewer

Agents must follow these skills when designing or generating code.

---

# Backend Development Guidelines

Backend code lives in:

backend/
Structure:
backend
├ api
├ models
├ services
└ agents


Rules:

- API routes belong in `backend/api`
- Business logic belongs in `backend/services`
- Data models belong in `backend/models`
- Avoid mixing business logic inside API routes
- Services must remain modular

---

# Frontend Development Guidelines

Frontend code lives in:
frontend/
Structure:
frontend
├ app
├ components
└ lib

Rules:

- Pages go in `app`
- Reusable UI components go in `components`
- Utilities go in `lib`
- Components should remain small and composable

---

# Database Guidelines

Database schema lives in:
database/


Rules:

- Always create migrations for schema changes
- Use clear naming conventions
- Avoid destructive schema changes
- Prefer additive migrations

---

# Code Quality Rules

Agents must follow these rules:

1. Prefer simple and readable code
2. Avoid large functions
3. Remove duplicate logic
4. Handle edge cases
5. Include error handling
6. Maintain modular design
7. Write tests for critical logic

---

# Testing

Tests should be written using **Test Driven Development (TDD)** when possible.

Testing layers include:

- Unit tests
- Integration tests
- End-to-end tests

The `/tdd` command should be used when implementing critical logic.

---

# Command Usage

Available commands:
/plan
/code-review
/python-review
/refactor-clean
/build-fix
/tdd


Commands must trigger the appropriate agent.

---

# Local Model Setup

Agents use local models via **Ollama**.

Model assignments:

Planner / Architect  
Model: `qwen2.5-coder`

Code Generation  
Model: `deepseek-coder`

Review / Debug  
Model: `qwen2.5-coder`

Agents should optimize prompts for these models.

---

# Development Principles

Agents should follow these principles:

- Plan before coding
- Prefer modular architecture
- Reuse existing patterns
- Follow repository structure
- Minimize unnecessary complexity
- Always consider edge cases
- Document architectural decisions

---

# Important Rule

Agents must **never start coding immediately**.

Every feature must first go through:

/plan

Only after the user confirms the plan should implementation begin.

When a task requires writing or modifying repository files:

1. Claude analyzes the problem
2. Claude prepares an implementation instruction
3. Claude calls the Aider tool to execute it
4. Claude reviews the result