#!/bin/bash

# Python Virtual Environment Setup Script for Newgame Project
# This script automates the creation and setup of a Python virtual environment

set -e  # Exit on any error

echo "🎮 Setting up Python virtual environment for Newgame project..."

# Check if Python 3.12 is available
if ! command -v python3.12 &> /dev/null; then
    if ! command -v python3 &> /dev/null; then
        echo "❌ Error: Python 3 is not installed or not in PATH"
        exit 1
    fi
    PYTHON_CMD="python3"
    echo "⚠️  Warning: python3.12 not found, using python3 instead"
else
    PYTHON_CMD="python3.12"
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "🐍 Using Python version: $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    $PYTHON_CMD -m venv venv
else
    echo "📦 Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
# Detect OS and use appropriate activation script
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]] || [[ -f "venv/Scripts/activate" ]]; then
    # Windows (Git Bash, MSYS2, etc.)
    source venv/Scripts/activate
else
    # Linux/macOS
    source venv/bin/activate
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies with retry logic
echo "📚 Installing dependencies from requirements.txt..."
MAX_RETRIES=3
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if pip install --timeout 300 --retries 2 -r requirements.txt; then
        echo "✅ Dependencies installed successfully!"
        break
    else
        RETRY_COUNT=$((RETRY_COUNT + 1))
        if [ $RETRY_COUNT -lt $MAX_RETRIES ]; then
            echo "⚠️  Installation failed, retrying ($RETRY_COUNT/$MAX_RETRIES)..."
            sleep 5
        else
            echo "❌ Failed to install dependencies after $MAX_RETRIES attempts."
            echo "💡 This may be due to network connectivity issues."
            echo "💡 You can manually install dependencies later with:"
            echo "   source venv/bin/activate"
            echo "   pip install -r requirements.txt"
            echo ""
        fi
    fi
done

echo "✅ Setup complete!"
echo ""
echo "📋 To activate the virtual environment in the future, run:"
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]] || [[ -f "venv/Scripts/activate" ]]; then
    echo "   source venv/Scripts/activate  # For Git Bash/MSYS2"
    echo "   venv\\Scripts\\activate.bat    # For Command Prompt"
    echo "   venv\\Scripts\\Activate.ps1   # For PowerShell"
else
    echo "   source venv/bin/activate"
fi
echo ""
echo "📋 To deactivate the virtual environment, run:"
echo "   deactivate"
echo ""
echo "🎮 You're now ready to start developing the Newgame project!"