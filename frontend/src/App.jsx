import { useEffect, useState } from 'react'
import { msalInstance } from './auth/msalConfig'
import './App.css'
import Login from './components/Login'
import Dashboard from './components/Dashboard'

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

  return isAuthenticated ? <Dashboard /> : <Login />
}

export default App
