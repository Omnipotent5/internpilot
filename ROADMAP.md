# ROADMAP.md

## Project Name
InternPilot

## Goal

Build an AI-powered system that helps students discover startups, generate personalized internship applications, and track application outcomes through a dashboard.

The roadmap defines the **development phases** and **feature milestones** for the system.

Agents must follow this roadmap when planning implementations.

---

# Development Philosophy

The system should be built incrementally.

Each phase should produce a **working feature set** that can be tested before moving to the next phase.

Agents should avoid implementing features from later phases unless explicitly instructed.

---

# Phase 1 — Core Backend Foundation

Goal: Establish the backend infrastructure and database.

Tasks:

- Setup FastAPI backend
- Define project structure
- Setup database connection
- Create core database schema

Database tables:

- users
- companies
- job_descriptions
- applications
- resumes
- cover_letters
- email_drafts

Backend modules:
backend
├ api
├ models
├ services
└ agents


Endpoints to create:
GET /companies
POST /companies
GET /applications
POST /applications


Success criteria:

- Backend runs successfully
- Database tables exist
- Basic CRUD operations work

---

# Phase 2 — Startup Discovery System

Goal: Automatically discover potential companies to apply to.

Features:

- company discovery from sources
- scraping or API integration
- store company data in database

Data collected:

- company name
- website
- hiring page
- job listings

Backend services:
company_discovery_service
company_data_parser


Success criteria:

- system can discover and store companies
- duplicate companies avoided

---

# Phase 3 — Job Description Analysis

Goal: Analyze job postings to extract useful signals.

Features:

- job description parsing
- skill extraction
- role categorization

Extracted information:

- required skills
- preferred skills
- technologies
- responsibilities

AI components:
job_description_analyzer
skill_extractor


Success criteria:

- system extracts structured data from job descriptions

---

# Phase 4 — Resume Personalization Engine

Goal: Generate tailored resumes for each company.

Features:

- resume parser
- resume modification
- highlight relevant skills

Capabilities:

- reorder resume sections
- emphasize relevant projects
- tailor bullet points

Outputs:

- personalized resume document
- PDF generation

Success criteria:

- system produces tailored resumes for different roles

---

# Phase 5 — Cover Letter Generator

Goal: Automatically generate personalized cover letters.

Inputs:

- job description
- company information
- user resume

AI system generates:

- personalized cover letter
- company-specific messaging

Success criteria:

- cover letters feel personalized and relevant

---

# Phase 6 — Human Approval Workflow

Goal: Ensure users approve all applications before sending.

User approval required for:

- resume
- cover letter
- email draft

Dashboard features:

- preview resume
- preview cover letter
- approve / edit application

Success criteria:

- system never sends emails without approval

---

# Phase 7 — Application Tracking Dashboard

Goal: Track internship applications in one place.

Dashboard should show:

- discovered companies
- prepared applications
- sent applications
- responses received
- interview status

Frontend features:
dashboard
company view
application status


Success criteria:

- user can track all applications easily

---

# Phase 8 — Email Automation

Goal: Generate and send application emails.

Features:

- email draft generation
- email preview
- manual send approval

Email content:

- introduction
- resume attachment
- cover letter attachment

Success criteria:

- emails generated correctly
- attachments included

---

# Phase 9 — AI Optimization

Goal: Improve personalization quality.

Improvements:

- better job matching
- better resume tailoring
- improved cover letter tone
- smarter company prioritization

Potential features:

- ranking companies by relevance
- suggesting best companies to apply to

---

# Phase 10 — Scaling & Automation

Goal: Make the system scalable.

Enhancements:

- queue-based processing
- caching
- background tasks
- improved scraping

Future possibilities:

- multi-user support
- cloud deployment
- analytics dashboard

---

# Future Ideas

Potential expansions:

- LinkedIn job integration
- recruiter contact discovery
- interview preparation assistant
- application success analytics
- AI networking outreach

---

# Important Rule for Agents

When implementing features:

1. Follow roadmap phases.
2. Avoid skipping phases.
3. Implement smallest working solution first.
4. Prefer incremental development.
5. Ensure each phase is testable.