"""
User interface elements for the Beaver Survival Game.
"""

import pygame
from ..config.constants import COLORS
from ..config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FOOD


class UI:
    """Manages all UI elements including HUD and menus."""

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 48)

    def draw_hud(self, screen, food_amount):
        """Draw the heads-up display."""
        # Food supply display in upper-left
        food_text = f"Food: {food_amount}/{MAX_FOOD}"
        food_color = COLORS["RED"] if food_amount <= MAX_FOOD * 0.2 else COLORS["WHITE"]

        food_surface = self.font.render(food_text, True, food_color)
        screen.blit(food_surface, (10, 10))

        # Optional: Add background for better readability
        text_rect = food_surface.get_rect()
        text_rect.x = 10
        text_rect.y = 10
        text_rect.inflate_ip(10, 5)
        pygame.draw.rect(screen, (0, 0, 0, 128), text_rect)
        screen.blit(food_surface, (10, 10))

    def draw_game_over_screen(self, screen, survival_time):
        """Draw the game over screen."""
        # Create semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(COLORS["BLACK"])
        screen.blit(overlay, (0, 0))

        # Game Over text
        game_over_text = self.large_font.render("Game Over", True, COLORS["WHITE"])
        game_over_rect = game_over_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60)
        )
        screen.blit(game_over_text, game_over_rect)

        # Survival time
        time_text = f"You survived: {survival_time} seconds"
        time_surface = self.font.render(time_text, True, COLORS["WHITE"])
        time_rect = time_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10)
        )
        screen.blit(time_surface, time_rect)

        # Restart instruction
        restart_text = "Press R to restart"
        restart_surface = self.font.render(restart_text, True, COLORS["YELLOW"])
        restart_rect = restart_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
        )
        screen.blit(restart_surface, restart_rect)

    def draw_pause_menu(self, screen):
        """Draw the pause menu."""
        # Create semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(COLORS["BLACK"])
        screen.blit(overlay, (0, 0))

        # Menu background
        menu_width, menu_height = 300, 200
        menu_rect = pygame.Rect(
            (SCREEN_WIDTH - menu_width) // 2,
            (SCREEN_HEIGHT - menu_height) // 2,
            menu_width,
            menu_height,
        )
        pygame.draw.rect(screen, COLORS["GRAY"], menu_rect)
        pygame.draw.rect(screen, COLORS["WHITE"], menu_rect, 3)

        # Pause title
        pause_text = self.large_font.render("Paused", True, COLORS["WHITE"])
        pause_rect = pause_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60)
        )
        screen.blit(pause_text, pause_rect)

        # Resume button
        resume_text = self.font.render("Resume (ESC)", True, COLORS["WHITE"])
        resume_rect = resume_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10)
        )
        screen.blit(resume_text, resume_rect)

        # Quit instruction
        quit_text = self.font.render("Quit (Q)", True, COLORS["WHITE"])
        quit_rect = quit_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
        )
        screen.blit(quit_text, quit_rect)

        return {"resume": resume_rect, "quit": quit_rect}

    def draw_instructions(self, screen):
        """Draw basic control instructions (optional for MVP)."""
        instructions = [
            "WASD or Arrow Keys: Move",
            "SPACE: Bite",
            "ESC: Pause",
            "R: Restart (when game over)",
        ]

        y_offset = SCREEN_HEIGHT - len(instructions) * 25 - 10
        for i, instruction in enumerate(instructions):
            text_surface = self.small_font.render(instruction, True, COLORS["WHITE"])
            # Add background for readability
            text_rect = text_surface.get_rect()
            text_rect.x = 10
            text_rect.y = y_offset + i * 25
            text_rect.inflate_ip(5, 2)
            pygame.draw.rect(screen, (0, 0, 0, 128), text_rect)
            screen.blit(text_surface, (10, y_offset + i * 25))
