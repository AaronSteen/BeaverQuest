"""
Food system for the Beaver Survival Game.
"""

import pygame
import random
from ..config.settings import (
    FOOD_SIZE,
    FOOD_SPAWN_INTERVAL,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DAM_HEIGHT,
)
from ..config.constants import COLORS


class FoodItem:
    """A collectible food item."""

    def __init__(self, x, y, food_type="berry"):
        self.rect = pygame.Rect(x, y, FOOD_SIZE, FOOD_SIZE)
        self.food_type = food_type
        self.color = COLORS["RED"] if food_type == "berry" else COLORS["DARK_GREEN"]

    def draw(self, screen):
        """Draw the food item."""
        pygame.draw.ellipse(screen, self.color, self.rect)
        # Add a small highlight
        highlight_rect = pygame.Rect(
            self.rect.x + 1, self.rect.y + 1, FOOD_SIZE - 2, FOOD_SIZE - 2
        )
        pygame.draw.ellipse(screen, COLORS["WHITE"], highlight_rect, 1)

    def get_collision_rect(self):
        """Get the collision rectangle."""
        return self.rect


class FoodManager:
    """Manages food item spawning and collection."""

    def __init__(self, lodge_rect, dam_rect):
        self.food_items = []
        self.lodge_rect = lodge_rect
        self.dam_rect = dam_rect
        self.last_spawn_time = pygame.time.get_ticks()
        self.spawn_interval = random.randint(*FOOD_SPAWN_INTERVAL)

    def update(self):
        """Update food spawning."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.spawn_interval:
            self._spawn_food()
            self.last_spawn_time = current_time
            self.spawn_interval = random.randint(*FOOD_SPAWN_INTERVAL)

    def _spawn_food(self):
        """Spawn a new food item in a valid location."""
        max_attempts = 50
        for _ in range(max_attempts):
            x = random.randint(FOOD_SIZE, SCREEN_WIDTH - FOOD_SIZE)
            y = random.randint(DAM_HEIGHT + FOOD_SIZE, SCREEN_HEIGHT - FOOD_SIZE)

            # Create temporary rect to check collision
            temp_rect = pygame.Rect(x, y, FOOD_SIZE, FOOD_SIZE)

            # Check if position is valid (not overlapping lodge or dam)
            if not temp_rect.colliderect(self.lodge_rect) and not temp_rect.colliderect(
                self.dam_rect
            ):

                # Randomly choose food type
                food_type = random.choice(["berry", "leaf"])
                self.food_items.append(FoodItem(x, y, food_type))
                break

    def check_collection(self, player_rect):
        """Check if player collected any food items and return collected items."""
        collected = []
        remaining = []

        for food in self.food_items:
            if player_rect.colliderect(food.get_collision_rect()):
                collected.append(food)
            else:
                remaining.append(food)

        self.food_items = remaining
        return collected

    def draw(self, screen):
        """Draw all food items."""
        for food in self.food_items:
            food.draw(screen)

    def clear(self):
        """Clear all food items."""
        self.food_items.clear()
