import '../styles/Footer.css'

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        
        {/* Footer Content Grid */}
        <div className="footer-grid">
          
          {/* Column 1: Brand */}
          <div className="footer-column">
            <div className="footer-brand">
              <span className="footer-logo-icon">∞</span>
              <span className="footer-logo-text">ResumeOptimizer</span>
            </div>
            <p className="footer-description">
              AI-powered resume optimization for job seekers.
            </p>
          </div>

          {/* Column 2: Product */}
          <div className="footer-column">
            <h4>Product</h4>
            <ul>
              <li><a href="#features">Features</a></li>
              <li><a href="#templates">Templates</a></li>
              <li><a href="#pricing">Pricing</a></li>
              <li><a href="#changelog">Changelog</a></li>
            </ul>
          </div>

          {/* Column 3: Company */}
          <div className="footer-column">
            <h4>Company</h4>
            <ul>
              <li><a href="#about">About</a></li>
              <li><a href="#blog">Blog</a></li>
              <li><a href="#careers">Careers</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div>

          {/* Column 4: Legal */}
          <div className="footer-column">
            <h4>Legal</h4>
            <ul>
              <li><a href="#privacy">Privacy Policy</a></li>
              <li><a href="#terms">Terms of Service</a></li>
              <li><a href="#cookies">Cookie Policy</a></li>
            </ul>
          </div>

        </div>

        {/* Footer Divider */}
        <div className="footer-divider"></div>

        {/* Footer Bottom */}
        <div className="footer-bottom">
          <p>&copy; 2026 ResumeOptimizer. All rights reserved.</p>
          <div className="footer-socials">
            <a href="https://twitter.com" title="Twitter">𝕏</a>
            <a href="https://linkedin.com" title="LinkedIn">in</a>
            <a href="https://github.com" title="GitHub">⚙</a>
          </div>
        </div>

      </div>
    </footer>
  )
}
