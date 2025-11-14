#!/usr/bin/env python3
"""
Test script to validate the Memory Game setup
"""

import os
import sys

def test_dependencies():
    """Test if all required dependencies are available"""
    try:
        from PIL import Image, ImageTk
        print("✅ Pillow (PIL) available")
    except ImportError:
        print("❌ Pillow (PIL) not found - run: pip install Pillow")
        return False
    
    try:
        import tkinter as tk
        print("✅ Tkinter available")
    except ImportError:
        print("❌ Tkinter not found - please install tkinter")
        return False
    
    return True

def test_assets():
    """Test if all game assets are in the correct locations"""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one level from scripts/
    themes = ['jelly', 'cats', 'food', 'bunny']
    missing_files = []
    
    # Check theme images
    for theme in themes:
        for i in range(1, 9):
            if theme == 'cats':
                file_path = os.path.join(base_dir, 'assets', 'images', 'themes', theme, f'cat{i}.png')
            else:
                theme_name = theme[:-1] if theme.endswith('s') else theme
                file_path = os.path.join(base_dir, 'assets', 'images', 'themes', theme, f'{theme_name}{i}.png')
            
            if not os.path.exists(file_path):
                missing_files.append(file_path)
    
    # Check back image
    back_path = os.path.join(base_dir, 'assets', 'images', 'ui', 'back.png')
    if not os.path.exists(back_path):
        missing_files.append(back_path)
    
    if missing_files:
        print("❌ Missing asset files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ All asset files found")
        return True

def test_game_import():
    """Test if the game module can be imported"""
    try:
        # Add parent directory to path to find memory_game.py
        import sys
        parent_dir = os.path.dirname(os.path.dirname(__file__))
        sys.path.insert(0, parent_dir)
        
        # Test import without running mainloop
        import memory_game
        print("✅ Game module imports successfully")
        return True
    except Exception as e:
        print(f"❌ Game import failed: {e}")
        return False

def main():
    print("🎮 Memory Game - System Test")
    print("=" * 40)
    
    tests_passed = 0
    total_tests = 3
    
    # Test dependencies
    if test_dependencies():
        tests_passed += 1
    
    # Test assets
    if test_assets():
        tests_passed += 1
    
    # Test game import (skip mainloop)
    if test_game_import():
        tests_passed += 1
    
    print("=" * 40)
    print(f"Tests passed: {tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The game is ready to run.")
        print("💡 Run: python3 memory_game.py")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())