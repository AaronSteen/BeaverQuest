# Overview
A game where you play as a beaver and collect resources from the surrounding woodland, with the goal of avoiding dying.

Visually, it's a top-down, 2-D game in the vein of Zelda: Link to the Past.

## Technical Implementation (MVP)
- **Game Engine**: Pygame
- **Screen Resolution**: 800x600 pixels
- **Frame Rate**: 60 FPS
- **Development Priority**: Get basic gameplay loop running onscreen as quickly as possible

## Game world
Represented as data, the game world will be a 9x9 2-D coordinate plane, zero-indexed, so that the northwest screen is at coordinate [0, 0].

When the game begins, you start in the exact center of the game world, at coordinate [4, 4], called `HOME_SCREEN`.

**MVP Note**: Start with just the HOME_SCREEN for initial development. Additional screens can be added once core mechanics are proven.

### HOME_SCREEN
This screen will contain:
- A lodge that is the beaver's home, and
- along the north border of the screen, the dam.
- The screen that is north of the dam is inaccessible because it is blocked by the dam.

The screens to the east, south, and west of the dam will be the only other areas accessible to the player at the start of the game.

This screen will contain the Lodge that is a "safe zone" and is the beaver's home.

## Input
- The player can move with `WASD` keys or the `Up`, `Left`, `Down`, `Right` arrow keys.
- The player can bite with `SPACE`.
- The `Esc` key pauses the game and opens the pause menu.
- All other keys have no use.

## Gameplay mechanics
This section describes the systems of the game world.

### Food storage
At the start of the game, the food storage value is 120.
Decreases by 1 unit every 4 seconds.
If the storage reaches zero, the game is over.
When the player collects [**food-item**], the storage is increased by 5.
The maximum food storage value is 200.

### Food items (MVP)
- **Appearance**: Simple colored circles or squares
- **Spawn**: Randomly appear on the HOME_SCREEN (avoiding lodge and dam areas)
- **Collection**: Player touches/overlaps with food item to collect
- **Respawn**: New food items appear every 10-15 seconds to maintain gameplay flow

### Victory/Failure Conditions
- **Game Over**: Food storage reaches 0
- **Feedback**: Display "Game Over - You survived X seconds" message
- **Restart**: Simple mechanism to restart the game (press R key or click button)

## Game Menus

### Start screen
To be implemented in a later version.

### Player HUD screen
This is where game information is displayed to the player. The Player HUD screen is transparent, only the items on it are visible.

#### Food supply bar
Represented by a rectangular bar in the upper-left of the Player HUD.
The length of the food supply bar is dependent on the food supply.
When the food supply is greater than 20% of max capacity, the bar is yellow.
When the food supply is 20% or less than max capacity, the bar turns red.

**MVP Alternative**: Start with simple text display "Food: 120/200" before implementing visual bar.

### Game Over screen
- Display "Game Over" message in center of screen
- Show survival time: "You survived: XX seconds"
- Show restart instruction: "Press R to restart"
- Dim background by 50%

### Pause menu
- Displays two buttons in the center of the screen, one above the other: `Resume` and `Quit`
- When the pause menu is activated, the game screen is dimmed 50%



## Sound
**MVP**: Sound effects are optional for initial version - focus on core gameplay first.

## Graphics
**MVP Asset Requirements** (keep simple for rapid prototyping):
- **Player (Beaver)**: Brown circle or simple rectangle (20x20 pixels)
- **Lodge**: Gray/brown rectangle (60x40 pixels) 
- **Dam**: Blue/gray horizontal line along north border
- **Food Items**: Small colored circles (red berries, green leaves)
- **Background**: Simple green color for grass/ground
- **Screen Size**: 800x600 pixels total

**Visual Priority Order**:
1. Functional colored shapes (Phase 1)
2. Simple sprites with basic detail (Phase 2) 
3. Polished art assets (Phase 3+)

## Development Phases

### Phase 1: Basic Prototype (MVP)
- Static HOME_SCREEN with moveable player character
- Simple collision detection for boundaries
- Basic colored shapes for all game objects

### Phase 2: Core Mechanics
- Food timer system with countdown display
- Collectible food items that spawn and respawn
- Food collection increases player's food storage

### Phase 3: Game States
- Game over detection and screen
- Restart functionality
- Basic pause menu

### Phase 4: Polish & Expansion
- Improved graphics and animations
- Sound effects and music
- Additional screens and world expansion
- Enhanced UI elements
