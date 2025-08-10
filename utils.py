"""
Utility functions and constants for the Beaver Survival Game.
"""

import pygame

# Screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Game world constants
HOME_SCREEN_COORD = [4, 4]  # Starting position in 9x9 world grid

# Player constants
PLAYER_SIZE = 20
PLAYER_SPEED = 3
PLAYER_SPEED_LAND = 2  # Slower on land

# Game object sizes
LODGE_WIDTH = 60
LODGE_HEIGHT = 40
DAM_HEIGHT = 10
FOOD_SIZE = 8

# Food system constants
INITIAL_FOOD = 120
MAX_FOOD = 200
FOOD_DECREASE_INTERVAL = 4000  # 4 seconds in milliseconds
FOOD_DECREASE_AMOUNT = 1
FOOD_COLLECTION_AMOUNT = 5
FOOD_SPAWN_INTERVAL = (10000, 15000)  # 10-15 seconds in milliseconds

# Colors (RGB)
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "BROWN": (139, 69, 19),
    "GREEN": (34, 139, 34),
    "BLUE": (70, 130, 180),
    "GRAY": (128, 128, 128),
    "RED": (255, 0, 0),
    "YELLOW": (255, 255, 0),
    "DARK_GREEN": (0, 100, 0),
    "DIM_OVERLAY": (0, 0, 0, 128),  # Semi-transparent black
}

# Zone types
ZONE_LODGE = "lodge"
ZONE_WATER = "water"
ZONE_LAND = "land"

# Game states
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAME_OVER = "game_over"

# Input keys
MOVEMENT_KEYS = {
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}


def clamp(value, min_value, max_value):
    """Clamp a value between min and max."""
    return max(min_value, min(value, max_value))


def rect_collision(rect1, rect2):
    """Check if two rectangles collide."""
    return rect1.colliderect(rect2)


def distance(pos1, pos2):
    """Calculate distance between two positions."""
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
