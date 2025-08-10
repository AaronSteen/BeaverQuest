"""
Entry point for the Beaver Survival Game.
"""

import sys
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
