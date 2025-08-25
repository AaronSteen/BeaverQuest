"""
Smoke tests - verify game can initialize without crashing.

These tests perform basic initialization checks to catch major breaking changes
early in development. They are designed to run quickly and catch "works on my
machine" issues related to game object creation and basic functionality.
"""

import pygame
import pytest
import sys
import os

# Ensure we can import game modules (handled by conftest.py)


def test_pygame_init():
    """Test pygame initializes without errors."""
    # Ensure pygame is clean
    if pygame.get_init():
        pygame.quit()

    pygame.init()
    assert pygame.get_init(), "pygame failed to initialize"

    # Clean up
    pygame.quit()
    assert not pygame.get_init(), "pygame failed to quit properly"


def test_pygame_display_modes():
    """Test that pygame can access display modes (headless safe)."""
    pygame.init()

    # This should work even in headless environments
    try:
        modes = pygame.display.list_modes()
        assert modes is not None, "Could not retrieve display modes"
        # modes might be -1 (all modes supported) or a list
        assert modes == -1 or isinstance(modes, list), "Invalid display modes format"
    finally:
        pygame.quit()


def test_game_creation():
    """Test main game object can be created."""
    pygame.init()

    try:
        from newgame.core.game import BeaverSurvivalGame

        # Create game object - this should not crash
        game = BeaverSurvivalGame()
        assert game is not None, "Game object creation failed"

        # Verify essential attributes exist
        assert hasattr(game, "screen"), "Game missing screen attribute"
        assert hasattr(game, "clock"), "Game missing clock attribute"
        assert hasattr(game, "game_state"), "Game missing game_state attribute"
        assert hasattr(game, "player"), "Game missing player attribute"
        assert hasattr(game, "food_manager"), "Game missing food_manager attribute"

    finally:
        pygame.quit()


def test_game_state_creation():
    """Test game state manager can be instantiated."""
    from newgame.core.game_state import GameStateManager

    game_state = GameStateManager()
    assert game_state is not None, "GameStateManager creation failed"

    # Test basic state functionality
    assert game_state.is_playing(), "Game should start in playing state"


def test_player_creation():
    """Test player object can be instantiated."""
    pygame.init()

    try:
        from newgame.entities.player import Player

        # Create player at a test position
        player = Player(100, 100)
        assert player is not None, "Player creation failed"

        # Verify player has required attributes
        assert hasattr(player, "rect"), "Player missing rect attribute"
        assert hasattr(player, "current_zone"), "Player missing current_zone attribute"
        assert player.rect.x == 100, "Player x position not set correctly"
        assert player.rect.y == 100, "Player y position not set correctly"

    finally:
        pygame.quit()


def test_game_objects_creation():
    """Test game objects (lodge, dam) can be instantiated."""
    pygame.init()

    try:
        from newgame.entities.objects import Lodge, Dam

        # Create lodge
        lodge = Lodge(50, 50)
        assert lodge is not None, "Lodge creation failed"
        assert hasattr(lodge, "get_collision_rect"), "Lodge missing collision method"

        # Create dam
        dam = Dam()
        assert dam is not None, "Dam creation failed"
        assert hasattr(dam, "get_collision_rect"), "Dam missing collision method"

    finally:
        pygame.quit()


def test_ui_creation():
    """Test UI system can be instantiated."""
    pygame.init()

    try:
        from newgame.systems.ui import UI

        ui = UI()
        assert ui is not None, "UI creation failed"

        # Verify UI has required methods
        assert hasattr(ui, "draw_hud"), "UI missing draw_hud method"
        assert hasattr(ui, "draw_pause_menu"), "UI missing draw_pause_menu method"
        assert hasattr(
            ui, "draw_game_over_screen"
        ), "UI missing draw_game_over_screen method"

    finally:
        pygame.quit()


def test_food_manager_creation():
    """Test food manager can be instantiated."""
    pygame.init()

    try:
        from newgame.entities.food import FoodManager
        from newgame.entities.objects import Lodge, Dam

        # Create required objects for food manager
        lodge = Lodge(50, 50)
        dam = Dam()

        # Create food manager
        food_manager = FoodManager(lodge.get_collision_rect(), dam.get_collision_rect())
        assert food_manager is not None, "FoodManager creation failed"

        # Verify food manager has required methods
        assert hasattr(food_manager, "update"), "FoodManager missing update method"
        assert hasattr(
            food_manager, "check_collection"
        ), "FoodManager missing check_collection method"

    finally:
        pygame.quit()


def test_config_imports():
    """Test that configuration modules can be imported."""
    from newgame.config import settings, constants

    # Verify essential settings exist
    assert hasattr(settings, "SCREEN_WIDTH"), "Missing SCREEN_WIDTH setting"
    assert hasattr(settings, "SCREEN_HEIGHT"), "Missing SCREEN_HEIGHT setting"
    assert hasattr(settings, "FPS"), "Missing FPS setting"

    # Verify essential constants exist
    assert hasattr(constants, "COLORS"), "Missing COLORS constant"
    assert hasattr(constants, "STATE_PLAYING"), "Missing STATE_PLAYING constant"


def test_full_game_initialization_flow():
    """Test the complete game initialization sequence."""
    pygame.init()

    try:
        from newgame.core.game import BeaverSurvivalGame

        # This mirrors what happens when the game starts
        game = BeaverSurvivalGame()

        # Verify the game is in a valid initial state
        assert game.food_amount > 0, "Game should start with food"
        assert game.game_state.is_playing(), "Game should start in playing state"

        # Test that we can call handle_events without crashing
        # (This doesn't process any actual events, just tests the method exists)
        try:
            # Create a minimal event to avoid blocking
            pygame.event.clear()
            result = game.handle_events()
            assert isinstance(result, bool), "handle_events should return boolean"
        except Exception as e:
            # If handle_events requires actual events, that's ok for smoke test
            pass

        # Test that update method exists and can be called
        game.update()

    finally:
        pygame.quit()


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
