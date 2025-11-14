#!/usr/bin/env python3
"""
Memory Game Launcher
Simple launcher script for the Memory Game
"""

import sys
import os

# Add the parent directory to the Python path to find memory_game.py
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

if __name__ == "__main__":
    try:
        # Import and run the main game
        from memory_game import main
        main()
    except ImportError:
        # Fallback to direct execution from parent directory
        import subprocess
        subprocess.run([sys.executable, os.path.join(parent_dir, "memory_game.py")])