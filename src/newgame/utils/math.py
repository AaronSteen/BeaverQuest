"""
Math and collision utility functions.
"""

import pygame


def clamp(value, min_value, max_value):
    """Clamp a value between min and max."""
    return max(min_value, min(value, max_value))


def distance(pos1, pos2):
    """Calculate distance between two positions."""
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def rect_collision(rect1, rect2):
    """Check if two rectangles collide."""
    return rect1.colliderect(rect2)
