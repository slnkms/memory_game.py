#!/usr/bin/env python3
"""
Simple setup script for Memory Game
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="memory-game",
    version="1.0.0",
    author="Memory Game Developer",
    description="A fun memory card matching game with multiple themes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["memory_game"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Pillow>=9.0.0",
    ],
    entry_points={
        "console_scripts": [
            "memory-game=memory_game:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["assets/images/**/*.png"],
    },
)