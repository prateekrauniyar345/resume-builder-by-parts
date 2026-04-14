#!/usr/bin/env python3
"""
Quick start guide for the Resume Optimizer system.
Run this script to get started in 5 minutes.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and report status."""
    print(f"\n{'='*60}")
    print(f"Step: {description}")
    print(f"{'='*60}")
    print(f"$ {cmd}\n")
    
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

def main():
    print("\n" + "="*60)
    print("🚀 Resume Optimizer - 5 Minute Quick Start")
    print("="*60)
    
    project_root = Path(__file__).parent
    
    # Step 1: Check prerequisites
    print("\n1️⃣  Checking prerequisites...")
    print("   ✓ Python 3 required")
    print("   ✓ Node.js required")
    print("   ✓ API key (OpenAI or Anthropic)")
    
    # Step 2: Backend setup
    print("\n2️⃣  Setting up backend...")
    backend_dir = project_root / "backend"
    if not (backend_dir / "venv").exists():
        run_command(
            "cd backend && python3 -m venv venv",
            "Creating virtual environment"
        )
    
    run_command(
        "cd backend && source venv/bin/activate && pip install -q -r ../requirements.txt",
        "Installing Python dependencies"
    )
    
    # Check .env file
    if not (backend_dir / ".env").exists():
        print("\n   ⚠️  Creating .env template...")
        (backend_dir / ".env").write_text(
            "# Add your API key here\n"
            "# OPENAI_API_KEY=sk-...\n"
            "# OR\n"
            "# ANTHROPIC_API_KEY=sk-ant-...\n"
        )
        print("   📝 Edit backend/.env with your API key")
    
    # Step 3: Frontend setup
    print("\n3️⃣  Setting up frontend...")
    frontend_dir = project_root / "frontend"
    if not (frontend_dir / "node_modules").exists():
        run_command(
            "cd frontend && npm install -q",
            "Installing Node dependencies"
        )
    
    # Step 4: Final instructions
    print("\n" + "="*60)
    print("✅ Setup Complete!")
    print("="*60)
    
    print("\n📋 Next Steps:")
    print("\n1. Configure your API key:")
    print("   Edit: backend/.env")
    print("   Add:  OPENAI_API_KEY=sk-... (or ANTHROPIC_API_KEY)")
    
    print("\n2. Start Backend (Terminal 1):")
    print("   cd backend")
    print("   source venv/bin/activate")
    print("   python server.py")
    print("   ✓ Backend runs on http://localhost:8000")
    
    print("\n3. Start Frontend (Terminal 2):")
    print("   cd frontend")
    print("   npm run dev")
    print("   ✓ Frontend runs on http://localhost:5173")
    
    print("\n4. Test the system:")
    print("   python test_system.py")
    
    print("\n5. Open in browser:")
    print("   http://localhost:5173")
    
    print("\n" + "="*60)
    print("📚 Documentation:")
    print("="*60)
    print("   • README.md - Overview & quick reference")
    print("   • SETUP.md - Detailed setup guide")
    print("   • IMPLEMENTATION.md - Architecture & how it works")
    print("   • test_system.py - System validation")
    
    print("\n" + "="*60)
    print("💡 Pro Tips:")
    print("="*60)
    print("   • Keep raw-docs updated for better context")
    print("   • Edit resume-parts/*.tex to customize base content")
    print("   • Detailed job descriptions = better optimizations")
    print("   • First run takes 30-60 sec (LLM processing)")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed: {e}")
        sys.exit(1)
