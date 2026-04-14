import { useState } from 'react'
import './App.css'
import ResumeOptimizer from './components/ResumeOptimizer'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Resume Optimizer</h1>
      </header>
      
      <main className="app-main">
        <ResumeOptimizer />
      </main>
      
      <footer className="app-footer">
        <p>&copy; 2026 AI Resume Optimizer | Powered by CrewAI</p>
      </footer>
    </div>
  )
}

export default App
