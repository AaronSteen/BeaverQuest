"""
Game settings and configuration constants.
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
