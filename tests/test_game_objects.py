"""
Tests for game objects.
"""

import pytest
import pygame
from newgame.entities.objects import Lodge, Dam
from newgame.entities.food import FoodItem, FoodManager
from newgame.config.settings import (
    LODGE_WIDTH,
    LODGE_HEIGHT,
    DAM_HEIGHT,
    SCREEN_WIDTH,
    FOOD_SIZE,
)


class TestGameObjects:
    """Test game objects functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        pygame.init()

    def test_lodge_creation(self):
        """Test lodge is created correctly."""
        lodge = Lodge(100, 150)
        assert lodge.rect.x == 100
        assert lodge.rect.y == 150
        assert lodge.rect.width == LODGE_WIDTH
        assert lodge.rect.height == LODGE_HEIGHT

    def test_dam_creation(self):
        """Test dam is created correctly."""
        dam = Dam()
        assert dam.rect.x == 0
        assert dam.rect.y == 0
        assert dam.rect.width == SCREEN_WIDTH
        assert dam.rect.height == DAM_HEIGHT

    def test_food_item_creation(self):
        """Test food item is created correctly."""
        food = FoodItem(50, 75, "berry")
        assert food.rect.x == 50
        assert food.rect.y == 75
        assert food.rect.width == FOOD_SIZE
        assert food.rect.height == FOOD_SIZE
        assert food.food_type == "berry"

    def test_food_manager_initialization(self):
        """Test food manager is initialized correctly."""
        lodge_rect = pygame.Rect(100, 150, LODGE_WIDTH, LODGE_HEIGHT)
        dam_rect = pygame.Rect(0, 0, SCREEN_WIDTH, DAM_HEIGHT)

        food_manager = FoodManager(lodge_rect, dam_rect)
        assert len(food_manager.food_items) == 0
        assert food_manager.lodge_rect == lodge_rect
        assert food_manager.dam_rect == dam_rect
