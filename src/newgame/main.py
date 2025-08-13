"""
Entry point for the Beaver Survival Game.
"""

import os
import sys
from .core.game import BeaverSurvivalGame


def main():
    """Entry point for the game."""
    # Optional debugpy integration for debugging
    if os.getenv("DEBUGPY_ENABLE") == "1":
        import debugpy

        debugpy.listen(("0.0.0.0", 5678))
        print("Waiting for debugger attach...")
        debugpy.wait_for_client()
        print("Debugger attached!")

    try:
        game = BeaverSurvivalGame()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
