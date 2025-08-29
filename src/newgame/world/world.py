"""
World for the Beaver Survival Game.
"""

import pygame

from ..config.constants import (
    WORLD_SIZE_X,
    WORLD_SIZE_Y,
)

class World:
    def __init__(self):
        self.size_y = WORLD_SIZE_Y
        self.size_x = WORLD_SIZE_X
        self.world_screens = (
                                ( (y, x) for x in range(self.size_x) ) 
                                    for y in range(self.size_y)
                             )


    

