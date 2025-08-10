# DESIGN DOC

## Overview
A game where you play as a beaver and collect resources from the surrounding woodland, with the goal of avoiding dying.

Visually, it's a top-down, 2-D game in the vein of Zelda: Link to the Past.

Represented as data, the game world will be a 9x9 2-D coordinate plane, zero-indexed, so that the northwest screen is at coordinate 0, 0. 

When the game begins, you start in the screen at the exact center of the plane, at coordinate 4, 4.

This screen will contain:
- A lodge that is the beaver's home, and
- along the north border of the screen, the dam. 
- The screen that is north of the dam is inaccessible because it is blocked by the dam.

The screens to the east, south, and west of the dam will be the only other areas accessible to the player at the start of the game.


