"""
Tests for player functionality.
"""

import pytest
import pygame
from newgame.entities.player import Player
from newgame.config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE


class TestPlayer:
    """Test player functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        pygame.init()
        self.player = Player(100, 100)
        # Create dummy rects for collision testing
        self.lodge_rect = pygame.Rect(50, 50, 60, 40)
        self.dam_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 10)

    def test_player_initialization(self):
        """Test player is initialized correctly."""
        assert self.player.rect.x == 100
        assert self.player.rect.y == 100
        assert self.player.rect.width == PLAYER_SIZE
        assert self.player.rect.height == PLAYER_SIZE

    def test_player_reset_position(self):
        """Test player position reset."""
        self.player.reset_position(200, 200)
        assert self.player.rect.x == 200
        assert self.player.rect.y == 200

    def test_collision_rect(self):
        """Test collision rectangle is correct."""
        collision_rect = self.player.get_collision_rect()
        assert collision_rect == self.player.rect
