import { useState } from 'react'
import '../styles/ResumeOptimizer.css'

export default function ResumeOptimizer() {
  const [jobDescription, setJobDescription] = useState('')
  const [jobTitle, setJobTitle] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [pdfLoading, setPdfLoading] = useState(false)

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

  const handleViewPdf = async () => {
    setPdfLoading(true)
    try {
      alert('PDF conversion feature coming soon! You can compile the LaTeX code in Overleaf.')
    } catch (err) {
      alert('Error generating PDF: ' + err.message)
    } finally {
      setPdfLoading(false)
    }
  }

  return (
    <div className="optimizer-container">
      <div className="two-column-layout">
        {/* Left Column */}
        <div className="left-column">
          <div className="section-card">
            <h2>Job Description</h2>
            
            <div className="form-group">
              <label htmlFor="jobTitle">Job Title (Optional)</label>
              <input
                id="jobTitle"
                type="text"
                placeholder="e.g., Senior Full Stack Engineer"
                value={jobTitle}
                onChange={(e) => setJobTitle(e.target.value)}
                disabled={loading}
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label htmlFor="jobDescription">Paste Job Description</label>
              <textarea
                id="jobDescription"
                placeholder="Paste the job description here..."
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                disabled={loading}
                className="form-textarea"
              />
              <div className="char-count">{jobDescription.length} characters</div>
            </div>

            <button
              onClick={handleOptimize}
              disabled={loading || !jobDescription.trim()}
              className="btn-primary"
            >
              {loading ? '⏳ Optimizing...' : 'Optimize Resume'}
            </button>
            
            {error && <div className="error-box">{error}</div>}
          </div>
        </div>

        {/* Right Column */}
        <div className="right-column">
          {!result ? (
            <div className="section-card empty-state">
              <p>Your optimized LaTeX resume will appear here</p>
            </div>
          ) : (
            <div className="section-card">
              <div className="result-header">
                <h2>Optimized Resume</h2>
                <div className="button-group">
                  <button
                    onClick={handleViewPdf}
                    disabled={pdfLoading}
                    className="btn-secondary"
                    title="View as PDF (like Overleaf)"
                  >
                    {pdfLoading ? '⏳ Generating...' : '📄 View PDF'}
                  </button>
                  <button
                    onClick={() => downloadResume(result.resume_content, result.filename)}
                    className="btn-secondary"
                    title="Download LaTeX file"
                  >
                    ⬇ Download
                  </button>
                  <button
                    onClick={() => copyToClipboard(result.resume_content)}
                    className="btn-secondary"
                    title="Copy to clipboard"
                  >
                    📋 Copy
                  </button>
                </div>
              </div>

              <div className="latex-preview">
                <pre>{result.resume_content}</pre>
              </div>

              <div className="file-info">
                <small>📁 Saved to: <code>{result.filename}</code></small>
              </div>
            </div>
          )}
        </div>
      </div>
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
