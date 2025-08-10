#!/usr/bin/env python3
"""
Game launcher script for development.
"""

import sys
import os

# Add src directory to path so we can import newgame
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
sys.path.insert(0, src_path)

from newgame.main import main

if __name__ == "__main__":
    main()
