"""
World for the Beaver Survival Game.
"""

import pygame

from ..config.settings import (
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
    HOME_SCREEN_Y,
)

class WorldScreen: # feels most natural to call it "Screen" but Screen is also a pygame object
    def __init__(self, coord_y, coord_x):
        self.coord_y = coord_y
        self.coord_x = coord_x
        self.water_rect = pygame.Rect(20, 20, (SCREEN_WIDTH-40), (SCREEN_HEIGHT-40))

    def draw(self, screen):
        pygame.draw.rect(screen, COLORS["BLUE"], self.water_rect)

class World:
    def __init__(self):
        self.size_y = WORLD_SIZE_Y
        self.size_x = WORLD_SIZE_X
        self.world_screens = [[WorldScreen(y, x) for x in range(size_x)] for y in range(size_y)]
        self.home_screen = self.screens[HOME_SCREEN_Y][HOME_SCREEN_X]


    

