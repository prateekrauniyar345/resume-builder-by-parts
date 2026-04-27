import { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { msalInstance } from './auth/msalConfig'
import './App.css'
import Navigation from './components/Navigation'
import Dashboard from './components/Dashboard'
import SignIn from './components/SignIn'
import SignUp from './components/SignUp'

function App() {
  const [accounts, setAccounts] = useState([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Handle redirect callback
    msalInstance.handleRedirectPromise().then(() => {
      const accounts = msalInstance.getAllAccounts()
      setAccounts(accounts)
      setIsLoading(false)
    }).catch(() => {
      setIsLoading(false)
    })
  }, [])

  const isAuthenticated = accounts.length > 0

  if (isLoading) {
    return (
      <div className="app-loading">
        <div className="spinner"></div>
        <p>Loading...</p>
      </div>
    )
  }

  return (
    <Router>
      <Routes>
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/dashboard" element={isAuthenticated ? <Dashboard /> : <SignIn />} />
        <Route path="/" element={isAuthenticated ? <Dashboard /> : <Navigation />} />
      </Routes>
    </Router>
  )
}

export default App
