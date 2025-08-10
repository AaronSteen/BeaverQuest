"""
Game state management for the Beaver Survival Game.
"""

import pygame
from utils import STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER


class GameStateManager:
    """Manages the current game state and transitions between states."""

    def __init__(self):
        self.current_state = STATE_PLAYING
        self.previous_state = None
        self.game_start_time = pygame.time.get_ticks()
        self.pause_time = 0
        self.total_pause_duration = 0

    def set_state(self, new_state):
        """Change to a new game state."""
        if new_state != self.current_state:
            self.previous_state = self.current_state
            self.current_state = new_state

            # Handle state-specific logic
            if new_state == STATE_PAUSED:
                self.pause_time = pygame.time.get_ticks()
            elif self.previous_state == STATE_PAUSED:
                # Resuming from pause
                if self.pause_time > 0:
                    self.total_pause_duration += (
                        pygame.time.get_ticks() - self.pause_time
                    )
                    self.pause_time = 0

    def is_playing(self):
        """Return True if the game is in playing state."""
        return self.current_state == STATE_PLAYING

    def is_paused(self):
        """Return True if the game is paused."""
        return self.current_state == STATE_PAUSED

    def is_game_over(self):
        """Return True if the game is over."""
        return self.current_state == STATE_GAME_OVER

    def get_survival_time(self):
        """Get the total survival time in seconds."""
        current_time = pygame.time.get_ticks()
        if self.current_state == STATE_PAUSED:
            # Don't count current pause time
            total_time = (
                self.pause_time - self.game_start_time - self.total_pause_duration
            )
        else:
            # Count all time except pauses
            total_time = current_time - self.game_start_time - self.total_pause_duration
            if self.pause_time > 0:
                total_time -= current_time - self.pause_time

        return max(0, total_time // 1000)  # Convert to seconds

    def reset_game(self):
        """Reset the game state for a new game."""
        self.current_state = STATE_PLAYING
        self.previous_state = None
        self.game_start_time = pygame.time.get_ticks()
        self.pause_time = 0
        self.total_pause_duration = 0
