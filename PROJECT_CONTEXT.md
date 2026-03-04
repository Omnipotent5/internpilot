# PROJECT_CONTEXT.md

## Project Name
InternPilot

## Overview

InternPilot is an AI-powered system that automates the internship application process for students.

The system discovers startups, analyzes job descriptions, personalizes resumes, generates cover letters, and manages internship applications through a dashboard.

The goal is to reduce the manual effort required for applying to internships while increasing the quality and personalization of applications.

---

# Core Features

### 1. Startup Discovery

The system discovers startups from sources such as:

- startup directories
- job boards
- company websites
- LinkedIn

Data extracted includes:

- company name
- company website
- job posting
- required skills
- hiring contact (if available)

---

### 2. Job Description Analyzer

The system analyzes job descriptions using AI to extract:

- required skills
- preferred skills
- responsibilities
- company culture signals
- relevant technologies

This information is used to tailor the application.

---

### 3. Resume Personalization

The system modifies the user's resume for each company by:

- highlighting relevant projects
- prioritizing relevant skills
- aligning experience with the job description

A new PDF resume may be generated per company if necessary.

---

### 4. Cover Letter Generation

The system generates a personalized cover letter using:

- job description
- company background
- user experience and projects

Each cover letter should feel specific to the company.

---

### 5. Human-in-the-Loop Approval

Before any email is sent:

The user must approve:

- personalized resume
- cover letter
- email draft

No automated sending without approval.

---

### 6. Application Tracking Dashboard

The dashboard allows the user to track:

- companies discovered
- applications prepared
- emails sent
- responses received
- interview status

---

# System Architecture

The project follows a modular full-stack architecture.

## Backend

Backend is built with:

- Python
- FastAPI

Backend responsibilities:

- startup discovery
- job description analysis
- resume generation
- cover letter generation
- email preparation
- application tracking

Backend structure:
backend
├ api
├ models
├ services
└ agents


Rules:

- API endpoints go in `backend/api`
- Business logic goes in `backend/services`
- Database models go in `backend/models`

Avoid mixing business logic inside API routes.

---

## Frontend

Frontend is built with:

- Next.js
- React

Frontend responsibilities:

- dashboard UI
- resume preview
- approval workflow
- application tracking

Frontend structure:
frontend
├ app
├ components
└ lib


Rules:

- Pages go in `app`
- Reusable UI goes in `components`
- Utilities go in `lib`

---

## Database

Database uses PostgreSQL.

Responsibilities:

- store companies
- store job descriptions
- store applications
- store generated resumes
- store email drafts
- store response tracking

Database files live in:
database/


All schema changes must use migrations.

---

# AI System

The system uses a multi-agent architecture.

Agents include:

- Architect
- Planner
- Code Reviewer
- Python Reviewer
- Refactor Cleaner
- Build Error Resolver
- TDD Guide

Agents should collaborate during development.

---

# Development Workflow

All development must follow this workflow:

1. `/plan`  
   Generate an implementation plan.

2. User confirms plan.

3. Implementation begins.

4. `/code-review`  
   Review generated code.

5. `/refactor-clean`  
   Improve code quality.

6. `/build-fix`  
   Resolve runtime or build errors.

7. `/tdd`  
   Add tests where necessary.

---

# Skill System

The project uses Antigravity skills stored in:
skills/


Skill categories include:

Architecture
- api-design-principles
- api-patterns
- database-design
- database-architect

Backend
- python-fastapi-development
- python-development-python-scaffold
- python-patterns
- api-security-best-practices
- api-documentation

Frontend
- react-nextjs-development
- react-best-practices
- react-ui-patterns
- react-state-management

Quality
- python-testing-patterns
- debugging-strategies
- code-reviewer

Agents should consult relevant skills before producing output.

---

# Development Principles

Agents must follow these principles:

1. Plan before writing code
2. Prefer modular design
3. Keep functions small and readable
4. Avoid duplicated logic
5. Handle edge cases
6. Maintain clear separation of concerns
7. Write tests for important logic
8. Follow existing repository structure

---

# Important Constraints

- No automated emails without user approval.
- Resume generation must be customizable.
- Each application should feel personalized.
- The system must scale to hundreds of applications.

---

# Success Criteria

The system should enable a user to:

1. Discover relevant startups automatically.
2. Generate personalized applications quickly.
3. Review and approve applications easily.
4. Track internship applications in a single dashboard.