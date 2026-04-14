#!/bin/bash

# AI Resume Optimizer - Quick Start Script

echo "====================================="
echo "AI Resume Optimizer - Quick Start"
echo "====================================="
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Python $PYTHON_VERSION found"
echo ""

# Check Node version
echo "Checking Node.js version..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16 or higher."
    exit 1
fi

NODE_VERSION=$(node -v)
echo "✓ Node.js $NODE_VERSION found"
echo ""

# Setup backend
echo "Setting up backend..."
cd backend || exit 1

if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python dependencies..."
pip install -q -r ../requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  No .env file found. Creating template..."
    cat > .env << 'EOF'
# Set your LLM API key below
# For OpenAI:
# OPENAI_API_KEY=sk-...

# For Anthropic:
# ANTHROPIC_API_KEY=sk-ant-...
EOF
    echo "Please edit backend/.env and add your API key"
fi

cd .. || exit 1
echo "✓ Backend setup complete"
echo ""

# Setup frontend
echo "Setting up frontend..."
cd frontend || exit 1

if [ ! -d "node_modules" ]; then
    echo "Installing Node dependencies..."
    npm install -q
fi

cd .. || exit 1
echo "✓ Frontend setup complete"
echo ""

echo "====================================="
echo "✓ Setup Complete!"
echo "====================================="
echo ""
echo "To start the application:"
echo ""
echo "1. Terminal 1 - Start Backend:"
echo "   cd backend && source venv/bin/activate && python server.py"
echo ""
echo "2. Terminal 2 - Start Frontend:"
echo "   cd frontend && npm run dev"
echo ""
echo "Then open http://localhost:5173 in your browser"
echo ""
echo "For more information, see SETUP.md"
