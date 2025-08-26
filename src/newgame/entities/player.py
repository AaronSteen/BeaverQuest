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
        WORLD_SIZE_X,
        WORLD_SIZE_Y,
        HOME_SCREEN_X,
        HOME_SCREEN_Y
        )

# This class was extensively updated to track the player's position in the broader world;
#   explanatory comments may be found throughout.
#                               -AS, 8.26.25
class Player:
    """The beaver player character."""

# The world now comprises a 9x9, 0-indexed grid. Player class was updated with 
#   to track world_x and world_y variables that track the player's position
#   in the grid
    def __init__(self):
        self.rect = pygame.Rect(400, 300, PLAYER_SIZE, PLAYER_SIZE)
        self.current_zone = ZONE_LAND
        self.color = COLORS["BROWN"]
        self.world_x = HOME_SCREEN_X
        self.world_y = HOME_SCREEN_Y

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

        # Collision stuff.
        #       Decide whether to update the player's position in the world grid
        #           by checking whether they leave the screen.
        #
        #       Ensure the player's world position is within the bounds of the world;
        #               if not, reset it.
        #
        #       First do horizontal dimension, then vertical dimension.

        # Store old positions; we use these to reset if we exceed screen or world bounds
        old_screen_x, old_screen_y = self.rect.x, self.rect.y
        old_world_x, old_world_y = self.world_x, self.world_y

        # Horizontal dimension
        self.rect.x += dx

        if self.rect.left < 0:
            self.world_x -= 1
            if self.world_x < 0:
                self.rect.x = old_screen_x
                self.world_x = old_world_x
            else:
                self.rect.x = (SCREEN_WIDTH - PLAYER_SIZE)

        if self.rect.right > SCREEN_WIDTH:
            self.world_x += 1
            if self.world_x >= WORLD_SIZE_X:
                self.rect.x = old_screen_x
                self.world_x = old_world_x
            else:
                self.rect.x = 0

        if self._check_dam_collision(dam_rect):
            self.rect.x = old_screen_x

        # Vertical dimension
        self.rect.y += dy

        if self.rect.top < 0:
            self.world_y -= 1
            if self.world_y < 0:
                self.rect.y = old_screen_y
                self.world_y = old_world_y
            else:
                self.rect.y = (SCREEN_HEIGHT - PLAYER_SIZE)

        # Here we check to see if the player is trying to enter the home screen from the top;
        #   if so, we block them because the dam is there. Not sure if this makes much
        #   sense; couldn't the beaver just climb over the dam? And shouldn't there be some
        #   water on the other side of the dam? 
        if self.rect.bottom > SCREEN_HEIGHT:
            self.world_y += 1
            if ( (self.world_y >= WORLD_SIZE_Y) or ( (self.world_x == HOME_SCREEN_X) and (self.world_y == HOME_SCREEN_Y) ) ):
                self.rect.y = old_screen_y
                self.world_y = old_world_y
            else:
                self.rect.y = 0

        # Only check for dam collision if we're on the home screen
        if (self.world_x == HOME_SCREEN_X and
                self.world_y == HOME_SCREEN_Y):
            if self._check_dam_collision(dam_rect):
                self.rect.y = old_screen_y

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
