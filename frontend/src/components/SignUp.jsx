import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { msalInstance, loginRequest } from '../auth/msalConfig'
import '../styles/SignIn.css'

export default function SignUp() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  const handleMicrosoftSignUp = async () => {
    try {
      setIsLoading(true)
      setError(null)
      
      const response = await msalInstance.loginPopup(loginRequest)
      
      if (response && response.accessToken) {
        // Successfully authenticated
        window.location.href = '/dashboard'
      }
    } catch (err) {
      console.error('Sign up failed:', err)
      setError('Failed to create account. Please try again.')
      setIsLoading(false)
    }
  }

  return (
    <div className="auth-container">
      {/* Back to Home Link */}
      <a href="/" className="back-link">← Back to Home</a>

      <div className="auth-card signup-card">
        <div className="auth-form-side">
          {/* Logo */}
          <div className="auth-logo">
            <span className="logo-icon">∞</span>
            <span className="logo-text">ResumeOptimizer</span>
          </div>

          {/* Heading */}
          <h1 className="auth-title">Get Started for Free</h1>
          <p className="auth-subtitle">
            Create your account and start optimizing your resume with AI in minutes
          </p>

          {/* Error Message */}
          {error && (
            <div className="error-message">
              <span className="error-icon">⚠️</span>
              {error}
            </div>
          )}

          {/* Microsoft Sign Up Button */}
          <button
            onClick={handleMicrosoftSignUp}
            disabled={isLoading}
            className="btn-microsoft"
          >
          <svg width="20" height="20" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="1" y="1" width="9" height="9" fill="#F25022"/>
            <rect x="13" y="1" width="9" height="9" fill="#7FBA00"/>
            <rect x="1" y="13" width="9" height="9" fill="#00A4EF"/>
            <rect x="13" y="13" width="9" height="9" fill="#FFB900"/>
          </svg>
          {isLoading ? 'Creating account...' : 'Sign up with Microsoft'}
        </button>

          {/* Divider */}
          <div className="divider">
            <span>OR</span>
          </div>

          {/* Sign In Link */}
          <p className="auth-info">
            Already have an account?{' '}
            <a href="/signin" className="auth-link">
              Sign in here
            </a>
          </p>

          {/* Security Note */}
          <div className="security-note">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M12 22C6.477 22 2 17.523 2 12s4.477-10 10-10 10 4.477 10 10-4.477 10-10 10zm-1-7h2v2h-2v-2zm0-8h2v6h-2V7z"/>
            </svg>
            Your data is protected with Microsoft Azure security
          </div>
        </div>

        {/* Right Side - Benefits */}
        <div className="auth-info-side">
          <h3 style={{ fontSize: '1.4rem', fontWeight: '600', marginBottom: '30px', color: 'var(--color-text-primary)' }}>
            Why Choose ResumeOptimizer
          </h3>
          <div className="benefits-list">
            <div className="benefit">
              <span className="benefit-icon">✓</span>
              <span>AI-powered resume optimization with 4 specialized agents</span>
            </div>
            <div className="benefit">
              <span className="benefit-icon">✓</span>
              <span>Professional LaTeX templates optimized for ATS</span>
            </div>
            <div className="benefit">
              <span className="benefit-icon">✓</span>
              <span>Tailored resumes for any job in minutes</span>
            </div>
            <div className="benefit">
              <span className="benefit-icon">✓</span>
              <span>Instant download and easy customization</span>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="auth-footer">
        <a href="#privacy">Privacy Policy</a>
        <span className="dot">•</span>
        <a href="#terms">Terms of Service</a>
      </footer>
    </div>
  )
}
