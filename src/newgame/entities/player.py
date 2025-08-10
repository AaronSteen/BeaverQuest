"""
Player (beaver) character for the Beaver Survival Game.
"""

import pygame
from ..config.settings import (
    PLAYER_SIZE,
    PLAYER_SPEED,
    PLAYER_SPEED_LAND,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from ..config.constants import (
    COLORS,
    MOVEMENT_KEYS,
    ZONE_LODGE,
    ZONE_WATER,
    ZONE_LAND,
)


class Player:
    """The beaver player character."""

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.current_zone = ZONE_LAND
        self.color = COLORS["BROWN"]

    def update(self, keys_pressed, lodge_rect, dam_rect):
        """Update player position based on input and collisions."""
        if not any(keys_pressed.values()):
            return

        # Calculate movement
        dx, dy = 0, 0
        for key, (key_dx, key_dy) in MOVEMENT_KEYS.items():
            if keys_pressed.get(key, False):
                dx += key_dx
                dy += key_dy

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.707  # Approximately 1/sqrt(2)
            dy *= 0.707

        # Apply speed based on current zone
        speed = PLAYER_SPEED_LAND if self.current_zone == ZONE_LAND else PLAYER_SPEED
        dx *= speed
        dy *= speed

        # Store old position for collision detection
        old_x, old_y = self.rect.x, self.rect.y

        # Move horizontally
        self.rect.x += dx
        # Check horizontal collisions
        if (
            self.rect.left < 0
            or self.rect.right > SCREEN_WIDTH
            or self._check_dam_collision(dam_rect)
        ):
            self.rect.x = old_x

        # Move vertically
        self.rect.y += dy
        # Check vertical collisions
        if (
            self.rect.top < 0
            or self.rect.bottom > SCREEN_HEIGHT
            or self._check_dam_collision(dam_rect)
        ):
            self.rect.y = old_y

        # Update current zone
        self._update_zone(lodge_rect)

    def _check_dam_collision(self, dam_rect):
        """Check if player collides with the dam."""
        return self.rect.colliderect(dam_rect)

    def _update_zone(self, lodge_rect):
        """Update the current zone based on player position."""
        if self.rect.colliderect(lodge_rect):
            self.current_zone = ZONE_LODGE
        elif self.rect.centery < 100:  # Upper part of screen is water
            self.current_zone = ZONE_WATER
        else:
            self.current_zone = ZONE_LAND

    def bite(self):
        """Perform bite action (basic implementation)."""
        # For MVP, just a placeholder - could add animation or sound later
        pass

    def draw(self, screen):
        """Draw the player on the screen."""
        # Draw the beaver as a brown rectangle
        pygame.draw.rect(screen, self.color, self.rect)

        # If in water, show head above water (lighter brown circle)
        if self.current_zone == ZONE_WATER:
            head_rect = pygame.Rect(
                self.rect.centerx - 6, self.rect.centery - 6, 12, 12
            )
            pygame.draw.ellipse(screen, COLORS["BROWN"], head_rect)

    def get_collision_rect(self):
        """Get the collision rectangle for the player."""
        return self.rect

    def reset_position(self, x, y):
        """Reset player to a new position."""
        self.rect.x = x
        self.rect.y = y
        self.current_zone = ZONE_LAND
