"""
Main game class for the Beaver Survival Game.
"""

import pygame
import sys
from ..config.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    INITIAL_FOOD,
    MAX_FOOD,
    FOOD_DECREASE_INTERVAL,
    FOOD_DECREASE_AMOUNT,
    FOOD_COLLECTION_AMOUNT,
)
from ..config.constants import (
    COLORS,
    STATE_PLAYING,
    STATE_PAUSED,
    STATE_GAME_OVER,
)
from .game_state import GameStateManager
from ..entities.player import Player
from ..entities.objects import Lodge, Dam
from ..entities.food import FoodManager
from ..systems.ui import UI


class BeaverSurvivalGame:
    """Main game class that manages the entire game."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Beaver Survival Game")
        self.clock = pygame.time.Clock()

        # Game components
        self.game_state = GameStateManager()
        self.ui = UI()

        # Initialize game objects
        self._init_game_objects()

        # Game variables
        self.food_amount = INITIAL_FOOD
        self.last_food_decrease = pygame.time.get_ticks()

        # Input tracking
        self.keys_pressed = {}

    def _init_game_objects(self):
        """Initialize all game objects."""
        # Create lodge in center-left area
        lodge_x = SCREEN_WIDTH // 4 - 30
        lodge_y = SCREEN_HEIGHT // 2 - 20
        self.lodge = Lodge(lodge_x, lodge_y)

        # Create dam along north border
        self.dam = Dam()

        # Create player starting position (center of screen)
        player_x = SCREEN_WIDTH // 2 - 10
        player_y = SCREEN_HEIGHT // 2
        self.player = Player(player_x, player_y)

        # Create food manager
        self.food_manager = FoodManager(
            self.lodge.get_collision_rect(), self.dam.get_collision_rect()
        )

    def handle_events(self):
        """Handle all game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_state.is_playing():
                        self.game_state.set_state(STATE_PAUSED)
                    elif self.game_state.is_paused():
                        self.game_state.set_state(STATE_PLAYING)

                elif event.key == pygame.K_r and self.game_state.is_game_over():
                    self._restart_game()

                elif event.key == pygame.K_q and self.game_state.is_paused():
                    return False

                elif event.key == pygame.K_SPACE and self.game_state.is_playing():
                    self.player.bite()

        # Track pressed keys for continuous movement
        if self.game_state.is_playing():
            keys = pygame.key.get_pressed()
            self.keys_pressed = {
                pygame.K_w: keys[pygame.K_w],
                pygame.K_s: keys[pygame.K_s],
                pygame.K_a: keys[pygame.K_a],
                pygame.K_d: keys[pygame.K_d],
                pygame.K_UP: keys[pygame.K_UP],
                pygame.K_DOWN: keys[pygame.K_DOWN],
                pygame.K_LEFT: keys[pygame.K_LEFT],
                pygame.K_RIGHT: keys[pygame.K_RIGHT],
            }

        return True

    def update(self):
        """Update game logic."""
        if not self.game_state.is_playing():
            return

        # Update player
        self.player.update(
            self.keys_pressed,
            self.lodge.get_collision_rect(),
            self.dam.get_collision_rect(),
        )

        # Update food spawning
        self.food_manager.update()

        # Check food collection
        collected_food = self.food_manager.check_collection(
            self.player.get_collision_rect()
        )
        for food in collected_food:
            self.food_amount = min(MAX_FOOD, self.food_amount + FOOD_COLLECTION_AMOUNT)

        # Decrease food over time
        current_time = pygame.time.get_ticks()
        if current_time - self.last_food_decrease >= FOOD_DECREASE_INTERVAL:
            self.food_amount = max(0, self.food_amount - FOOD_DECREASE_AMOUNT)
            self.last_food_decrease = current_time

            # Check game over condition
            if self.food_amount <= 0:
                self.game_state.set_state(STATE_GAME_OVER)

    def draw(self):
        """Draw everything on the screen."""
        # Clear screen with green background (land)
        self.screen.fill(COLORS["GREEN"])

        # Draw water area (upper part of screen)
        water_rect = pygame.Rect(0, 10, SCREEN_WIDTH, 100)
        pygame.draw.rect(self.screen, COLORS["BLUE"], water_rect)

        # Draw game objects
        self.dam.draw(self.screen)
        self.lodge.draw(self.screen)
        self.food_manager.draw(self.screen)
        self.player.draw(self.screen)

        # Draw UI based on game state
        if self.game_state.is_playing() or self.game_state.is_paused():
            self.ui.draw_hud(self.screen, self.food_amount)

        if self.game_state.is_paused():
            self.ui.draw_pause_menu(self.screen)
        elif self.game_state.is_game_over():
            survival_time = self.game_state.get_survival_time()
            self.ui.draw_game_over_screen(self.screen, survival_time)

        pygame.display.flip()

    def _restart_game(self):
        """Restart the game to initial state."""
        self.game_state.reset_game()
        self.food_amount = INITIAL_FOOD
        self.last_food_decrease = pygame.time.get_ticks()

        # Reset player position
        player_x = SCREEN_WIDTH // 2 - 10
        player_y = SCREEN_HEIGHT // 2
        self.player.reset_position(player_x, player_y)

        # Clear all food items
        self.food_manager.clear()

        # Reset input
        self.keys_pressed = {}

    def run(self):
        """Main game loop."""
        running = True

        while running:
            # Handle events
            running = self.handle_events()

            # Update game logic
            self.update()

            # Draw everything
            self.draw()

            # Control frame rate
            self.clock.tick(FPS)

        pygame.quit()
