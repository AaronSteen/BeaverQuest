"""
Static constants for the game.
"""

import pygame

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
