import { useState } from 'react'
import { msalInstance, loginRequest } from '../auth/msalConfig'
import '../styles/Login.css'

export default function Login() {
  const [isLoading, setIsLoading] = useState(false)

  const handleLogin = async () => {
    try {
      setIsLoading(true)
      await msalInstance.loginPopup(loginRequest)
      window.location.reload()
    } catch (error) {
      console.error('Login failed:', error)
      setIsLoading(false)
    }
  }

  return (
    <div className="landing-page">
        
        {/* Navigation */}
        <nav 
          className="navbar"
          style={{
            backgroundColor: '#ffffff',
            padding: '12px',
            marginTop: '20px',
            borderRadius: '18px',
            border: '2px solid #e0e0e0',
          }}
        >
        
          <div className="nav-logo">
            <span className="logo-icon">∞</span>
            <span className="logo-text">ResumeOptimizer</span>
          </div>
          <div className="nav-links">
            <a href="#home">Home</a>
            <a href="#features">Features</a>
            <a href="#resources">Resources</a>
            <a href="#templates">Templates</a>
          </div>
          <div className="nav-actions">
            <button onClick={handleLogin} disabled={isLoading} className="btn-login">
              Log In
            </button>
            <button onClick={handleLogin} disabled={isLoading} className="btn-signup">
              {isLoading ? 'Signing up...' : 'Sign Up'}
            </button>
          </div>
        </nav>

        {/* Hero Section */}
        <section className="hero-section" id="home">
          <h1 className="hero-title">Build a Job-Winning<br/>Resume in Minutes with AI</h1>
          <p className="hero-subtitle">
            Our 4 parallel AI agents analyze your experience, skills, and career goals to craft a highly detailed, ATS-friendly resume perfectly tailored to your target job role.
          </p>
          <button onClick={handleLogin} disabled={isLoading} className="btn-primary">
            Build My Resume <span className="arrow">→</span>
          </button>

          <div className="hero-image-container">
            <img 
              src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?q=80&w=2070&auto=format&fit=crop" 
              alt="Person using laptop" 
              className="hero-img"
            />
            {/* Floating Badges */}
            <div className="floating-badge badge-score">
              <span className="text-orange">92%</span> Resume Score
            </div>
            <div className="floating-badge badge-ai">
              ✨ Ask AI Coach Anything...
            </div>
            <div className="floating-badge badge-skills">
              <div className="skills-header">
                <span>Skills</span>
                <span className="add-skill-btn">+ Add Skill</span>
              </div>
              <div className="skill-tags">
                <span className="skill-tag">Management Skills</span>
                <span className="skill-tag">Analytical thinking</span>
                <span className="skill-tag">Leadership</span>
              </div>
            </div>
          </div>
        </section>

        {/* Split Feature Section */}
        <section className="split-feature-section" id="features">
          <div className="split-image-side">
            <img 
              src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=1976&auto=format&fit=crop" 
              alt="Professional looking at camera" 
              className="split-img"
            />
            <div className="floating-badge badge-top-right">
              <p className="badge-title">Resume Match Score</p>
              <p className="badge-value text-green">+42% improvement</p>
            </div>
            <div className="floating-badge badge-bottom-left">
              <p className="badge-title">Build Time</p>
              <p className="badge-text">Under 5 minutes</p>
            </div>
            <div className="floating-badge badge-bottom-right">
              <p className="badge-title">Interview Callbacks</p>
              <p className="badge-value text-green">+18% increase</p>
            </div>
          </div>
          <div className="split-text-side">
            <h2 className="section-title text-left">AI-Powered Interview<br/>Ready Resumes</h2>
            <p className="section-description">
              ResumeOptimizer uses 4 specialized AI agents (Skills, Education, Experience, Projects) working in parallel to optimize every section of your resume. Improve visibility, relevance, and recruiter engagement across every application.
            </p>
            <button onClick={handleLogin} className="btn-secondary">
              See How It Works <span className="arrow">→</span>
            </button>
            <div className="stats-row">
              <div className="stat-box">
                <h3>40%</h3>
                <p>Higher ATS match rate</p>
              </div>
              <div className="stat-box">
                <h3>32%</h3>
                <p>More recruiter engagement</p>
              </div>
              <div className="stat-box">
                <h3>3x</h3>
                <p>Faster resume creation</p>
              </div>
            </div>
          </div>
        </section>

        {/* Grid Features Section */}
        <section className="grid-features-section">
          <h2 className="section-title text-center">Features That Make<br/>ResumeOptimizer Stand Out</h2>
          <p className="section-subtitle text-center">
            From multi-agent AI rewriting to LaTeX ATS optimization,<br/>everything you need for a job-winning resume.
          </p>
          
          <div className="features-grid">
            <div className="feature-card dark-card">
              <h3>Experience Agent Rewrites for You</h3>
              <p>Our Experience Agent analyzes your raw work history and rewrites bullet points with powerful metrics and action verbs, tailored perfectly to the job.</p>
              <div className="feature-illustration ui-mockup">
                <div className="mockup-header">Professional Summary</div>
                <div className="mockup-body text-small">
                  Experienced and effective Business Development manager bringing forth significant value and a genuine passion for management. With a proven track record of driving growth and fostering strong client relationships...
                </div>
              </div>
            </div>
            
            <div className="feature-card dark-card">
              <h3>Guided Parallel Optimization</h3>
              <p>Our 4 agents (Skills, Education, Experience, Projects) work simultaneously. Just follow the simple flow and finish in minutes.</p>
              <div className="feature-illustration ui-mockup">
                 <div className="mockup-step"><span className="check">✓</span> Step 1 • Personal Details</div>
                 <div className="mockup-step"><span className="check">✓</span> Step 2 • Job Description</div>
                 <div className="mockup-step active"><span className="check">✓</span> Step 3 • AI Optimization</div>
              </div>
            </div>

            <div className="feature-card light-green-card">
              <h3>Resume Quality Score</h3>
              <p>See how strong your resume really is. Get instant insights and clear improvement suggestions from our Skills Agent.</p>
              <div className="feature-illustration flex-center">
                 <div className="score-circle">
                   <span className="score-num">48%</span>
                   <span className="score-text">Need Improvement</span>
                 </div>
              </div>
            </div>

            <div className="feature-card brown-card">
              <h3>Match Any Job Instantly</h3>
              <p>Drop a job description text and let our Agents understand exactly what recruiters want. Your LaTeX resume gets tailored automatically.</p>
              <div className="feature-illustration ui-mockup">
                 <div className="mockup-input">Paste job description here...</div>
                 <div className="mockup-input-small">Target Job Title</div>
              </div>
            </div>
          </div>
        </section>

        {/* Why Choose Section */}
        <section className="why-choose-section" id="resources">
          <h2 className="section-title text-center">Why Choose ResumeOptimizer</h2>
          <p className="section-subtitle text-center">
            Smart multi-agent AI, professional LaTeX templates, and ATS-friendly<br/>resumes—everything you need to get hired faster.
          </p>
          <div className="center-btn-wrapper">
             <button onClick={handleLogin} className="btn-secondary">
                Build My Resume with AI <span className="arrow">→</span>
             </button>
          </div>

          <div className="global-stats-row">
            <div className="global-stat">
              <h4>Experience Launched</h4>
              <h3>Since 2024</h3>
              <p>Built with a mission to simplify resume creation using intelligent parallel automation.</p>
            </div>
            <div className="global-stat center-stat">
              <h4>AI Resumes Generated</h4>
              <h3 className="text-orange">100,000+</h3>
              <p>Thousands of personalized resumes crafted across roles, industries, and career levels.</p>
            </div>
            <div className="global-stat">
              <h4>User Success Score</h4>
              <h3>95%</h3>
              <p>Most users see improved ATS results and higher interview shortlisting rates.</p>
            </div>
          </div>
          
          <div className="why-images-row">
            <div className="why-img-box">
              <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=2070&auto=format&fit=crop" alt="Office" />
              <div className="img-badge">Pro Templates ✓</div>
            </div>
            <div className="why-img-box large">
              <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070&auto=format&fit=crop" alt="Team" />
              <div className="img-badge">AI Resume Writing ✓</div>
            </div>
            <div className="why-img-box">
              <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=2070&auto=format&fit=crop" alt="Success" />
              <div className="img-badge">Fast & Simple ✓</div>
            </div>
          </div>
        </section>

        {/* Templates Section */}
        <section className="templates-section" id="templates">
          <div className="templates-text">
            <h2 className="section-title text-left">Templates Designed<br/>for Real Hiring</h2>
            <p className="section-description">
              Professionally designed LaTeX resume templates to impress recruiters and pass ATS, optimized for clarity, readability, and modern hiring standards.
            </p>
            <button onClick={handleLogin} className="btn-secondary text-left-btn">
              View All Templates <span className="arrow">→</span>
            </button>
            <div className="templates-features">
              <div className="t-feature">
                <h4>Modern & Clean Layouts</h4>
                <p>Minimal, well-structured designs that highlight your skills and experience clearly.</p>
              </div>
              <div className="t-feature">
                <h4>ATS-Compatible Formats</h4>
                <p>All templates are natively generated in LaTeX to work seamlessly with Applicant Tracking Systems.</p>
              </div>
            </div>
          </div>
          <div className="templates-image">
            <img src="https://images.unsplash.com/photo-1573164713988-8665fc963095?q=80&w=2069&auto=format&fit=crop" alt="Professional working" />
            <div className="floating-badge badge-top-left">AI-Optimized Content Fit</div>
            <div className="floating-badge badge-bottom-right">Fully Customizable</div>
          </div>
        </section>

        {/* Footer */}
        <footer className="footer-section">
          <p>&copy; 2026 ResumeOptimizer. All rights reserved.</p>
        </footer>
    </div>
  )
}
