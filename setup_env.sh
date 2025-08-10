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
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "📋 To activate the virtual environment in the future, run:"
echo "   source venv/bin/activate"
echo ""
echo "📋 To deactivate the virtual environment, run:"
echo "   deactivate"
echo ""
echo "🎮 You're now ready to start developing the Newgame project!"