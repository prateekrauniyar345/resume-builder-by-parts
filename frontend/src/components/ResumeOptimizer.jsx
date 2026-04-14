import { useState } from 'react'
import '../styles/ResumeOptimizer.css'

export default function ResumeOptimizer() {
  const [jobDescription, setJobDescription] = useState('')
  const [jobTitle, setJobTitle] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleOptimize = async () => {
    setError(null)
    setLoading(true)

    try {
      const response = await fetch('http://localhost:8000/optimize-resume', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          job_description: jobDescription,
          job_title: jobTitle || 'Optimized Position',
        }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Failed to optimize resume')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message || 'An error occurred while optimizing your resume')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="optimizer-container">
      <div className="input-section">
        <h2>Paste Job Description</h2>
        <div className="input-group">
          <label htmlFor="jobTitle">Job Title (Optional)</label>
          <input
            id="jobTitle"
            type="text"
            placeholder="e.g., Senior Full Stack Engineer"
            value={jobTitle}
            onChange={(e) => setJobTitle(e.target.value)}
            disabled={loading}
          />
        </div>

        <div className="input-group">
          <label htmlFor="jobDescription">Job Description</label>
          <textarea
            id="jobDescription"
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            disabled={loading}
            rows={10}
          />
          <p className="char-count">
            {jobDescription.length} characters
          </p>
        </div>

        <button
          onClick={handleOptimize}
          disabled={loading || !jobDescription.trim()}
          className="optimize-btn"
        >
          {loading ? 'Optimizing Resume...' : 'Optimize Resume'}
        </button>
      </div>

      {error && (
        <div className="error-section">
          <h3>Error</h3>
          <p className="error-message">{error}</p>
        </div>
      )}

      {result && (
        <div className="result-section">
          <div className="result-header">
            <h2>Your Optimized Resume</h2>
            <div className="result-actions">
              <button
                onClick={() => downloadResume(result.resume_content, result.filename)}
                className="download-btn"
              >
                Download LaTeX
              </button>
              <button
                onClick={() => copyToClipboard(result.resume_content)}
                className="copy-btn"
              >
                Copy Content
              </button>
            </div>
          </div>

          <div className="file-info">
            <p><strong>Saved to:</strong> <code>{result.file_path}</code></p>
            <p><strong>Filename:</strong> <code>{result.filename}</code></p>
          </div>

          <div className="resume-preview">
            <h3>Resume Preview (Raw LaTeX)</h3>
            <pre>{result.resume_content}</pre>
          </div>
        </div>
      )}
    </div>
  )
}

function downloadResume(content, filename) {
  const element = document.createElement('a')
  const file = new Blob([content], { type: 'text/plain' })
  element.href = URL.createObjectURL(file)
  element.download = filename
  document.body.appendChild(element)
  element.click()
  document.body.removeChild(element)
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('Resume content copied to clipboard!')
  }).catch(() => {
    alert('Failed to copy to clipboard')
  })
}
