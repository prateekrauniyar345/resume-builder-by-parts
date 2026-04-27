# ResumeOptimizer - System Knowledge Base

## Introduction
ResumeOptimizer is a sophisticated, multi-agent AI application designed to dynamically tailor a candidate's resume to a specific job description. It maintains a base set of facts about the candidate and uses Large Language Models (LLMs) to restructure, highlight, and rewrite the resume for the best possible match, generating a professionally formatted LaTeX document.

## Architecture Overview

### Frontend
- **Framework**: React (using Vite)
- **Styling**: Vanilla CSS with a centralized variable system (`index.css`)
- **Authentication**: Microsoft Entra ID (Azure AD) via `@azure/msal-react`
- **Key Components**:
  - `Login.jsx`: The public-facing landing page showcasing the product's features (Hero, 4 Agents, Templates) and providing the entry point for login.
  - `Dashboard.jsx`: The authenticated user interface where users interact with the optimizer.
  - `ResumeOptimizer.jsx`: The core component handling job description input and displaying the resulting LaTeX output.

### Backend
- **Framework**: Python with FastAPI
- **AI Orchestration Layer**: LangChain / CrewAI
- **Data Flow**:
  - `backend/app/raw-docs/`: The "ground truth" source. Contains raw markdown files of the candidate's actual work history, projects, and background. This ensures agents never hallucinate skills or experiences.
  - `backend/app/resume-parts/`: Contains the LaTeX templates (`head.tex`, `skills.tex`, `experience.tex`, etc.) that get populated by the AI agents.
  - `backend/output/`: The destination where the final concatenated and optimized LaTeX `.tex` files are saved with timestamps.

## AI Agents Architecture
When a job description is submitted, the backend runs 4 autonomous agents in parallel to optimize different sections of the resume simultaneously:

1. **Skills Agent**: Extracts required tech stacks/skills from the job posting and matches/prioritizes them against the candidate's actual skills.
2. **Education Agent**: Highlights the most relevant coursework or academic achievements related to the role.
3. **Experience Agent**: Rewrites experience bullet points to include relevant keywords, emphasize matching achievements, and incorporate power verbs while strictly maintaining the truthfulness of the metrics.
4. **Projects Agent**: Reframes personal/portfolio projects to highlight the specific technologies mentioned in the job description.

## Workflow
1. User logs in via Microsoft Entra ID.
2. User pastes a Job Description into the React UI dashboard.
3. The FastAPI backend receives the description and loads the user's `raw-docs` and `resume-parts`.
4. The 4 AI agents run in parallel, communicating with the configured LLM.
5. The optimized parts are stitched together into a complete LaTeX file.
6. The frontend presents the user with the optimized resume for download.

## Deployment & Setup
- **Backend Setup**: Requires a Python 3.10+ virtual environment and `.env` configuration for the LLM Provider (OpenAI, Anthropic, Cerebras, Google Gemini).
- **Frontend Setup**: Requires Node.js 16+, `npm install`, and `.env` configuration for Azure AD (`VITE_AZURE_CLIENT_ID`, `VITE_AZURE_TENANT_ID`).
- Both servers can be run concurrently during development (`npm run dev` and `python server.py`).
