# AI Resume Optimizer

A sophisticated multi-agent resume optimization system powered by CrewAI. This application uses specialized AI agents to tailor your resume to any job description while maintaining authenticity.

## 🚀 Quick Start

```bash
# 1. Configure environment
cd backend
cp .env.example .env
# Edit .env and add your LLM API key (OpenAI or Anthropic)

# 2. Run setup script
cd ..
bash quickstart.sh

# 3. Start Backend (Terminal 1)
cd backend
source venv/bin/activate
python server.py

# 4. Start Frontend (Terminal 2)
cd frontend
npm run dev

# 5. Open browser
# http://localhost:5173
```

## 📋 System Overview

The system uses 4 specialized AI agents that work together to optimize your resume:

1. **Skills Optimizer** - Matches and prioritizes technical skills
2. **Education Optimizer** - Highlights relevant coursework and achievements
3. **Experience Optimizer** - Rewrites work bullets for relevance
4. **Projects Optimizer** - Reframes projects to emphasize job-relevant technologies

### How It Works

```
Job Description → 4 Agents Process in Parallel → Optimized Resume
                   ↓
            Uses Your Background Context
            (raw-docs folder)
                   ↓
            Maintains Authenticity While
            Tailoring to Job Requirements
```

## 📁 Project Structure

```
resume-builder/
├── backend/
│   ├── agents/              # CrewAI agents
│   │   ├── config.py       # System prompts for each agent
│   │   ├── crew.py         # Crew orchestration
│   │   └── utils.py        # Resume building utilities
│   ├── resume-parts/        # Modular LaTeX resume sections
│   ├── raw-docs/            # Your background documents
│   ├── output/              # Generated optimized resumes
│   └── server.py            # FastAPI backend
├── frontend/                # React application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── styles/          # CSS styles
│   │   └── App.jsx
│   └── package.json
├── requirements.txt         # Python dependencies
├── SETUP.md                 # Detailed setup guide
└── test_system.py          # System validation script
```

## ⚙️ Configuration

### Environment Variables

Create `backend/.env`:

```env
# Choose your LLM provider:

# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo

# OR Anthropic
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-opus-20240229
```

### Resume Content

- **Resume Sections**: Edit `.tex` files in `backend/resume-parts/`
- **Background Context**: Add documents to `backend/raw-docs/`
  - Work descriptions in `.md` format
  - Project details
  - Certifications
  - Any relevant background material

## 🧪 Testing

Validate your setup:

```bash
python test_system.py
```

This will test:
- Backend connectivity
- Resume parts loading
- Output directory
- Full optimization workflow (if API key configured)

## 📖 Usage

1. Copy a job description
2. Paste into the frontend
3. (Optional) Add job title
4. Click "Optimize Resume"
5. Download the generated LaTeX

Generated resumes are saved to `backend/output/` with timestamps.

## 🔌 API Endpoints

### POST `/optimize-resume`
Optimize resume for a job

**Request:**
```json
{
  "job_description": "Full job posting...",
  "job_title": "Senior Engineer"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Resume successfully optimized...",
  "resume_content": "LaTeX content...",
  "file_path": "/path/to/Resume_*.tex",
  "filename": "Resume_Senior_Engineer_*.tex"
}
```

### GET `/health`
Check if backend is running

### GET `/resume-parts`
View loaded resume sections

### GET `/output-directory`
Get path to generated resumes

## 🛠️ Development

### Backend Development
```bash
cd backend
source venv/bin/activate
python server.py
```

### Frontend Development
```bash
cd frontend
npm run dev
```

### Making Custom Changes

**Modify agent behavior:**
- Edit system prompts in `backend/agents/config.py`

**Update resume content:**
- Edit `.tex` files in `backend/resume-parts/`

**Add more context:**
- Add `.md` files to `backend/raw-docs/`

## 🚀 Production Deployment

**Frontend:**
```bash
cd frontend
npm run build
# Deploy dist/ folder to static hosting
```

**Backend:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 backend.server:app
```

## 🔍 Troubleshooting

**Backend won't start:**
- Check if `requirements.txt` packages installed: `pip list`
- Verify `.env` file exists and API key is set
- Try: `python -m backend.server`

**Frontend can't connect to backend:**
- Ensure backend is running on `http://localhost:8000`
- Check CORS is enabled (it should be by default)
- Clear browser cache and try again

**Optimization takes too long:**
- LLM calls typically take 30-60 seconds
- Check your API rate limits
- Verify API key is valid

**Generated resumes not saving:**
- Check `backend/output/` directory exists
- Verify write permissions: `chmod 755 backend/output/`
- Check disk space availability

## 📚 Additional Resources

- [SETUP.md](SETUP.md) - Detailed setup guide
- [CrewAI Documentation](https://docs.crewai.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [LaTeX Resume Guide](https://www.overleaf.com)

## ✨ Features

- ✅ 4 specialized AI agents working in parallel
- ✅ Context-aware optimization using your background
- ✅ LaTeX-based resume (complete formatting control)
- ✅ REST API for integration
- ✅ Clean React frontend
- ✅ Timestamp-based file management
- ✅ Download and copy functionality

## 🎯 Next Steps

1. Run `bash quickstart.sh` to set up everything
2. Configure your API key in `backend/.env`
3. Start backend and frontend
4. Test with `python test_system.py`
5. Optimize your first resume!

## 💡 Tips for Best Results

- Provide detailed job descriptions (200+ characters)
- Include specific technologies and tools in job posting
- Keep resume sections current with recent achievements
- Use specific metrics and numbers in raw-docs
- Review and edit generated LaTeX if needed

## 📝 License

MIT License - Feel free to customize and use for your resume optimization needs!

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to open an issue or submit a pull request!
