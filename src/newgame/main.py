"""
Entry point for the Beaver Survival Game.
"""

import os
import sys

# Debugpy integration for debugging - placed at top as requested
if os.getenv("DEBUGPY_ENABLE") == "1":
    import debugpy

    debugpy.listen(("localhost", 5678))  # Listen on port 5678
    print("Waiting for debugger attach...")
    debugpy.wait_for_client()  # Pause execution until VS Code attaches
    print("Debugger attached!")

from .core.game import BeaverSurvivalGame


def main():
    """Entry point for the game."""
    try:
        game = BeaverSurvivalGame()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
