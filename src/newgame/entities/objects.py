"""
Game objects for the Beaver Survival Game (Lodge, Dam).
"""

import pygame
from ..config.settings import (
    LODGE_WIDTH,
    LODGE_HEIGHT,
    DAM_HEIGHT,
    SCREEN_WIDTH,
)
from ..config.constants import COLORS


class Lodge:
    """The beaver's lodge - a safe zone."""

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, LODGE_WIDTH, LODGE_HEIGHT)
        self.color = COLORS["GRAY"]

    def draw(self, screen):
        """Draw the lodge."""
        pygame.draw.rect(screen, self.color, self.rect)
        # Add a simple outline
        pygame.draw.rect(screen, COLORS["BLACK"], self.rect, 2)

    def get_collision_rect(self):
        """Get the collision rectangle."""
        return self.rect


class Dam:
    """The dam along the north border - blocks access to the north."""

    def __init__(self):
        self.rect = pygame.Rect(0, 0, SCREEN_WIDTH, DAM_HEIGHT)
        self.color = COLORS["BLUE"]

    def draw(self, screen):
        """Draw the dam."""
        pygame.draw.rect(screen, self.color, self.rect)
        # Add gray accent to make it look more like a dam
        pygame.draw.rect(
            screen,
            COLORS["GRAY"],
            pygame.Rect(0, DAM_HEIGHT // 2, SCREEN_WIDTH, DAM_HEIGHT // 2),
        )

    def get_collision_rect(self):
        """Get the collision rectangle."""
        return self.rect
