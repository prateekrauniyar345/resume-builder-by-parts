# AI Resume Optimizer - Multi-Agent System

A sophisticated resume optimization system using CrewAI that tailors your resume to any job description. It features specialized AI agents for skills, education, experience, and projects sections.

## Features

- **4 Dedicated AI Agents**: Each agent specializes in a specific resume section
  - **Skills Optimizer**: Matches and prioritizes skills from job descriptions
  - **Education Optimizer**: Highlights relevant coursework and achievements
  - **Experience Optimizer**: Rewrites bullets to align with job requirements
  - **Projects Optimizer**: Reframes projects to emphasize job-relevant technologies

- **Smart Context Awareness**: Uses your raw documentation (work descriptions, project notes) to maintain authenticity
- **LaTeX-Based Resume**: Complete control over formatting with modular resume parts
- **REST API**: FastAPI backend for easy integration
- **Modern React Frontend**: User-friendly interface for submitting job descriptions and viewing results

## Project Structure

```
resume-builder/
├── backend/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── config.py           # Agent system prompts
│   │   ├── crew.py             # Multi-agent crew orchestration
│   │   └── utils.py            # Resume loading and building utilities
│   ├── resume-parts/           # Modular LaTeX resume sections
│   │   ├── head.tex
│   │   ├── skills.tex
│   │   ├── education.tex
│   │   ├── experience.tex
│   │   ├── projects.tex
│   │   └── tail.tex
│   ├── raw-docs/               # Context documents for agents
│   │   └── *.md, *.pdf, *.tex
│   ├── output/                 # Generated optimized resumes
│   └── server.py               # FastAPI server
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   └── ResumeOptimizer.jsx
│   │   ├── styles/
│   │   │   └── ResumeOptimizer.css
│   │   ├── App.jsx
│   │   └── ...
│   └── package.json
├── requirements.txt            # Python dependencies
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 16+
- An LLM API key (OpenAI, Anthropic, etc.)

### Backend Setup

1. **Create a Python virtual environment**:
   ```bash
   cd resume-builder
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the `backend/` directory:
   ```env
   # For OpenAI
   OPENAI_API_KEY=your_openai_api_key

   # OR for Anthropic
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

4. **Start the FastAPI server**:
   ```bash
   cd backend
   python server.py
   ```
   The server will run on `http://localhost:8000`

### Frontend Setup

1. **Install frontend dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server**:
   ```bash
   npm run dev
   ```
   The frontend will run on `http://localhost:5173`

## Usage

1. Open `http://localhost:5173` in your browser
2. Paste a job description in the "Job Description" field
3. (Optional) Enter the job title
4. Click "Optimize Resume"
5. View the optimized resume and download the LaTeX file

## How It Works

### Agent Workflow

1. **Input Analysis**: CrewAI receives the job description
2. **Parallel Processing**: 4 agents simultaneously optimize their respective sections:
   - Extract key requirements and keywords from the job posting
   - Review your current resume section
   - Rewrite/reorganize to match job requirements
   - Maintain authenticity using context from raw-docs
3. **Resume Assembly**: Combine all optimized sections with header and footer
4. **Output Generation**: Save the complete LaTeX resume

### System Prompts

Each agent has specialized system instructions:
- **Skills**: Keywords optimization, skill prioritization, grouping
- **Education**: Relevant coursework highlighting, GPA emphasis
- **Experience**: Bullet rewriting, power verbs, quantification
- **Projects**: Impact emphasis, technical skill alignment

## API Endpoints

### POST `/optimize-resume`
Optimize resume based on job description.

**Request**:
```json
{
  "job_description": "Full job posting text...",
  "job_title": "Senior Full Stack Engineer"
}
```

**Response**:
```json
{
  "status": "success",
  "message": "Resume successfully optimized...",
  "resume_content": "LaTeX resume content...",
  "file_path": "/path/to/resume.tex",
  "filename": "Resume_Senior_Full_Stack_Engineer_20240115_143022.tex"
}
```

### GET `/health`
Health check endpoint.

### GET `/resume-parts`
Get current resume sections (preview).

### GET `/output-directory`
Get the output directory path.

## Customization

### Updating Resume Sections

Edit the `.tex` files in `backend/resume-parts/`:
- All changes will be incorporated into optimized resumes
- The system maintains these as base-line content

### Adding Context

Add more context documents to `backend/raw-docs/`:
- `.md` files with work descriptions
- `.pdf` files with certifications
- Any relevant background material
- Helps agents make better optimization decisions

### Modifying Agent Behavior

Edit agent system prompts in `backend/agents/config.py`:
- Customize optimization rules
- Change emphasis areas
- Adjust for different role types

## Environment Variables

```env
# LLM Configuration
OPENAI_API_KEY=sk-...
# OR
ANTHROPIC_API_KEY=sk-ant-...

# Server Configuration (optional)
API_HOST=0.0.0.0
API_PORT=8000
```

## Troubleshooting

**API Connection Error**:
   - Ensure backend server is running on `http://localhost:8000`
   - Check CORS settings if using a different origin

**Agent Timeout**:
   - LLM API calls can take 30-60 seconds
   - Check your API key and rate limits

**Resume Not Saving**:
   - Ensure `backend/output/` directory exists
   - Check write permissions on the directory

## Performance Tips

- Provide detailed job descriptions (200+ characters recommended)
- Include specific technologies and tools in the job posting
- Keep resume sections up-to-date with latest achievements
- Use specific metrics and numbers in your raw-docs for better context

## Development

### Running Tests
```bash
pytest backend/tests/
```

### Building for Production

**Frontend**:
```bash
cd frontend
npm run build
```

**Backend**:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 backend.server:app
```

## Future Enhancements

- [ ] Support for multiple resume templates
- [ ] Batch job description processing
- [ ] Resume version history and comparison
- [ ] Cover letter generation
- [ ] LinkedIn profile optimization
- [ ] Real-time resume preview (PDF rendering)
- [ ] Database for saving past optimizations
- [ ] User authentication and personalization

## License

MIT License - feel free to use this for your resume optimization needs!

## Support

For issues or questions, check the troubleshooting section or review the agent system prompts to understand how decisions are made.
