# Overview
A game where you play as a beaver and collect resources from the surrounding woodland, with the goal of avoiding dying.

Visually, it's a top-down, 2-D game in the vein of Zelda: Link to the Past.

Represented as data, the game world will be a 9x9 2-D coordinate plane, zero-indexed, so that the northwest screen is at coordinate 0, 0.

When the game begins, you start in the screen at the exact center of the plane, at coordinate 4, 4.

This screen will contain:
- A lodge that is the beaver's home, and
- along the north border of the screen, the dam.
- The screen that is north of the dam is inaccessible because it is blocked by the dam.

The screens to the east, south, and west of the dam will be the only other areas accessible to the player at the start of the game.

This screen will contain the Lodge that is a "safe zone" and is the beaver's home. This screen

The game world will be stored as anWhen the game starts, the forest that serves as the game's setting should be represented by four separate screens.

## Input
- The player can move with `WASD` keys or the `Up`, `Left`, `Down`, `Right` arrow keys.
- The player can bite with `SPACE`.
- The player can grab with `F`.
- The `Esc` key pauses the game and opens the pause menu.
- All other keys have no use.

## Game Menus

### Start screen
To be implemented in a later version.

### Pause menu
- Displays two buttons in the center of the screen, one above the other: `Resume` and `Quit`
- When the pause menu is activated, the game screen is dimmed 50%

## Gameplay mechanics
This section describes the systems of the game world.

### Food supply
Decreases by 1 unit every 5 seconds.
Represented by a rectangular bar on the player HUD.
When over 20%, the bar is yellow.
When it reaches 20%, the bar turns red.
If supply reaches zero, the game is over.
When the player collects <food-item>, the supply is increased by 5.

###

## Sound

## Graphics
