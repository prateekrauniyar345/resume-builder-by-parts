import { useState, useEffect } from 'react'
import { msalInstance } from '../auth/msalConfig'
import '../styles/Dashboard.css'
import ResumeOptimizer from './ResumeOptimizer'

export default function Dashboard() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    const account = msalInstance.getActiveAccount()
    setUser(account)
  }, [])

  const handleLogout = async () => {
    await msalInstance.logoutPopup()
  }

  return (
    <div className="app-container">
      {/* Header/Navigation */}
      <header className="app-header">
        <div className="app-header-container">
          <div className="logo-section">
            <h1 className="logo">Resume Optimizer</h1>
          </div>
          <nav className="main-nav">
            <a href="#" className="nav-link">Dashboard</a>
            <a href="#" className="nav-link">History</a>
            <a href="#" className="nav-link">Help</a>
          </nav>
          <div className="user-menu">
            {user && (
              <>
                <span className="user-greeting">Welcome, {user.name?.split(' ')[0]}</span>
                <button onClick={handleLogout} className="btn-logout">Sign Out</button>
              </>
            )}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="app-main">
        <div className="app-width">
          {/* Page Header */}
          <div className="page-header">
            <h2>Resume Optimizer</h2>
            <p>Paste a job description and optimize your resume to match</p>
          </div>

          {/* Optimizer Section */}
          <div className="optimizer-container">
            <ResumeOptimizer />
          </div>
        </div>
      </main>
    </div>
  )
}
