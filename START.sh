#!/bin/bash

# 🎮 MEMORY GAME - ONE-CLICK LAUNCHER 🎮
# =====================================
# This script automatically sets up and launches the Memory Game
# No manual setup required - just run: ./START.sh

echo "🎮 Memory Game - One-Click Launcher"
echo "===================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    echo "Visit: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "⚠️  requirements.txt not found, installing Pillow manually..."
    pip install Pillow
fi

echo ""
echo "🚀 Launching Memory Game..."
echo "=============================="
python3 memory_game.py

# Deactivate virtual environment when game closes
deactivate