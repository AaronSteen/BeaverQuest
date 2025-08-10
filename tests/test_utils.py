"""
Tests for utility functions.
"""

import pytest
from newgame.utils.math import clamp, distance, rect_collision
import pygame


class TestMathUtils:
    """Test math utility functions."""

    def test_clamp(self):
        """Test the clamp function."""
        assert clamp(5, 0, 10) == 5
        assert clamp(-1, 0, 10) == 0
        assert clamp(15, 0, 10) == 10
        assert clamp(7.5, 5.0, 10.0) == 7.5

    def test_distance(self):
        """Test the distance function."""
        assert distance((0, 0), (0, 0)) == 0
        assert distance((0, 0), (3, 4)) == 5.0
        assert distance((1, 1), (4, 5)) == 5.0

    def test_rect_collision(self):
        """Test rectangle collision detection."""
        pygame.init()

        rect1 = pygame.Rect(0, 0, 10, 10)
        rect2 = pygame.Rect(5, 5, 10, 10)  # Overlapping
        rect3 = pygame.Rect(20, 20, 10, 10)  # Not overlapping

        assert rect_collision(rect1, rect2) == True
        assert rect_collision(rect1, rect3) == False
        assert rect_collision(rect2, rect3) == False
