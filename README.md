# AI Resume Optimizer

A sophisticated multi-agent resume optimization system with a modern dashboard and Microsoft Entra authentication. This application uses specialized AI agents to tailor your resume to any job description while maintaining authenticity.

## ✨ Features

- **Beautiful Dashboard** - Modern, responsive interface with multiple sections
- **Microsoft Authentication** - Secure sign-in with Microsoft Entra ID
- **AI-Powered Resume Optimization** - 4 specialized agents optimize different resume sections in parallel
- **LaTeX Export** - Professional resume generation with full control over formatting
- **Real-time Status** - See optimization progress and download results instantly

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm
- Python 3.10+
- Azure subscription (free tier available)
- LLM API key (OpenAI, Anthropic, Cerebras, or Google Gemini)

### Installation

```bash
# 1. Clone repository
cd resume-builder

# 2. Setup Backend
cd backend
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
pip install -r requirements.txt

# 3. Configure Backend
cp .env.template .env
# Edit .env with your LLM API key

# 4. Setup Frontend
cd ../frontend
npm install

# 5. Configure Azure AD
# See AZURE_SETUP.md for detailed instructions
cp .env.example .env
# Edit .env with your Azure AD credentials
```

### Running the Application

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python server.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Visit `http://localhost:5173` in your browser and sign in with Microsoft.

## 🎯 System Overview

### Architecture

```
User → Login (Microsoft Entra) → Dashboard → Resume Optimizer
                                    ↓
                              4 AI Agents (Parallel)
                              - Skills Matcher
                              - Education Highlighter
                              - Experience Rewriter
                              - Projects Reframer
                                    ↓
                              LaTeX Resume Generator
                                    ↓
                              Download / Save
```

### AI Agents

1. **Skills Optimizer** - Matches and prioritizes technical skills from job requirements
2. **Education Optimizer** - Highlights relevant coursework and academic achievements
3. **Experience Optimizer** - Rewrites work bullets for relevance with metrics
4. **Projects Optimizer** - Reframes projects to emphasize job-relevant technologies

All agents maintain authenticity by using your background documents as ground truth.

## 📁 Project Structure

```
resume-builder/
├── backend/
│   ├── app/
│   │   ├── agents/              # LangChain/LangGraph agents
│   │   │   ├── workflow.py      # Multi-agent state machine
│   │   │   ├── get_agent.py     # Agent factory
│   │   │   ├── get_llm.py       # LLM initialization
│   │   │   ├── config.py        # Agent system prompts
│   │   │   └── utils.py         # Resume utilities
│   │   ├── prompts/             # System prompts for each agent
│   │   ├── routes/              # FastAPI routes
│   │   ├── models/              # Pydantic response models
│   │   ├── resume-parts/        # LaTeX resume sections
│   │   ├── raw-docs/            # Background documents
│   │   └── output/              # Generated resumes
│   ├── server.py                # FastAPI application
│   ├── requirements.txt         # Python dependencies
│   └── .env                     # LLM configuration
├── frontend/
│   ├── src/
│   │   ├── auth/                # Microsoft Auth (MSAL)
│   │   │   ├── msalConfig.js    # MSAL configuration
│   │   │   └── AuthContext.jsx  # Auth state management
│   │   ├── components/
│   │   │   ├── Dashboard.jsx    # Main dashboard
│   │   │   ├── Login.jsx        # Login page
│   │   │   └── ResumeOptimizer.jsx
│   │   ├── styles/              # CSS styles
│   │   ├── App.jsx              # Main app component
│   │   └── main.jsx
│   ├── .env                     # Azure AD configuration
│   ├── vite.config.js           # Vite configuration
│   └── package.json
├── AZURE_SETUP.md               # Azure AD setup guide
├── SETUP.md                     # Detailed setup instructions
└── README.md                    # This file
```

## 🔐 Authentication

The application uses **Microsoft Entra ID** (Azure AD) for secure, enterprise-grade authentication.

### Setup Microsoft Authentication

1. Follow the [Azure AD Setup Guide](./AZURE_SETUP.md)
2. Get your Azure AD Application ID and Tenant ID
3. Configure `frontend/.env`:

```env
VITE_AZURE_CLIENT_ID=your_app_id
VITE_AZURE_TENANT_ID=common
VITE_AZURE_REDIRECT_URI=http://localhost:5173
```

### Authentication Flow

1. User clicks "Sign in with Microsoft"
2. Redirected to Microsoft login
3. User authenticates and grants permissions
4. Redirected back with authorization code
5. Access token obtained securely
6. User profile displayed in dashboard

## 🎨 Dashboard Features

### Resume Optimizer Tab
- Paste job description
- Specify job title (optional)
- See optimized resume in real-time
- Download LaTeX file
- Copy to clipboard

### History Tab
- View past optimizations
- Reuse previous resume versions
- Track optimization history

### Templates Tab
- Choose professional resume templates
- Modern, Classic, Creative options
- One-click template application

### Settings Tab
- Notification preferences
- Dark mode toggle
- Email subscription management
- Account preferences

## ⚙️ Backend Configuration

### Environment Variables

Create `backend/.env`:

```env
# LLM Provider Configuration
LLM_PROVIDER="openai"  # or "anthropic", "cerebras", "genai"
LLM_MODEL="gpt-4-mini"
LLM_API_KEY=sk-...
```

### Supported LLM Providers

- **OpenAI**: `gpt-4-mini`, `gpt-4-turbo`
- **Anthropic**: `claude-3-opus`, `claude-3-sonnet`
- **Cerebras**: `qwen-3-235b-a22b-instruct-2507`
- **Google Gemini**: `gemini-2.5-flash-lite`

### Resume Parts

All resume sections are stored as LaTeX templates in `backend/app/resume-parts/`:
- `head.tex` - Name, contact info
- `skills.tex` - Technical skills
- `education.tex` - Degree and coursework
- `experience.tex` - Work history
- `projects.tex` - Portfolio projects
- `tail.tex` - Certifications, awards

### Background Documents

Add context to `backend/app/raw-docs/`:
- Work descriptions (markdown)
- Project details
- Certifications
- Achievement highlights
- Any relevant background material

## 🚀 API Endpoints

### Health Checks
- `GET /api/backend-health` - Backend status
- `GET /api/llm-health` - LLM provider status
- `GET /api/llm-provider` - LLM configuration info

### Resume Optimization
- `POST /api/optimize-resume` - Optimize resume for job description
  
**Request:**
```json
{
  "job_description": "Full job posting text...",
  "job_title": "Senior Full Stack Engineer"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Resume successfully optimized",
  "resume_content": "LaTeX content...",
  "file_path": "/path/to/resume.tex",
  "filename": "Resume_..."
}
```

## 📊 Resume Optimization Process

1. **Load Context**: Retrieve current resume and background documents
2. **Parse Job**: Extract requirements and keywords from job description
3. **Parallel Processing**: Run 4 agents simultaneously
   - Skills agent matches and prioritizes skills
   - Education agent highlights relevant coursework
   - Experience agent rewrites bullets with metrics
   - Projects agent reframes projects for relevance
4. **Combine**: Assemble optimized sections with header/footer
5. **Generate**: Create final LaTeX resume with timestamp
6. **Return**: Send to frontend for download/display

## 🛠️ Development

### Install Dependencies
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### Run Development Servers
```bash
# Backend (Terminal 1)
cd backend && python server.py

# Frontend (Terminal 2)
cd frontend && npm run dev
```

### Build for Production
```bash
# Backend
cd backend
# Deploy with gunicorn or similar

# Frontend
cd frontend
npm run build
# Deploy dist/ folder
```

## 📝 Customization

### Adding New Resume Sections
1. Create new `.tex` file in `backend/app/resume-parts/`
2. Update `ResumeLoader.load_all_resume_parts()` in `utils.py`
3. Create corresponding agent prompt

### Changing Agent Behavior
Edit system prompts in `backend/app/prompts/`:
- `skills_agent_prompt.py`
- `education_agent_prompt.py`
- `experience_agent_prompt.py`
- `projects_agent_prompt.py`

### Modifying Resume Output
Edit LaTeX templates in `backend/app/resume-parts/` directly. Changes automatically apply to all generated resumes.

## 🐛 Troubleshooting

### Login Issues
- Check Azure AD configuration in AZURE_SETUP.md
- Verify `frontend/.env` values match Azure app registration
- Check browser console for MSAL errors

### Resume Generation Fails
- Check LLM API key in `backend/.env`
- Verify LLM provider is accessible
- Check backend logs for detailed errors
- Ensure all resume parts exist in `backend/app/resume-parts/`

### CORS Errors
- Frontend and backend URLs should match
- Check CORS configuration in `backend/server.py`
- Update allowed origins for your deployment

### Optimization Takes Too Long
- Some LLM providers are slower than others
- Check LLM health: `GET /api/llm-health`
- Consider using faster models (GPT-4-mini, Gemini-Flash)

## 📚 Additional Resources

- [Azure AD Setup Guide](./AZURE_SETUP.md) - Complete Microsoft authentication setup
- [Detailed Setup Instructions](./SETUP.md) - Step-by-step installation
- [Implementation Details](./IMPLEMENTATION.md) - Architecture deep dive
- [Microsoft Entra Documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
- [MSAL React Documentation](https://github.com/AzureAD/microsoft-authentication-library-for-js/)

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
