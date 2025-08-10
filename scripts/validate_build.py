#!/usr/bin/env python3
"""
Quick smoke test - verify all core imports work.

This script performs a basic validation of the build by attempting to import
all core game modules and verifying that pygame is available. It's designed
to catch "works on my machine" issues early in development.

Usage: python scripts/validate_build.py
Exit Code: 0 for success, 1 for failure
"""

import sys
from pathlib import Path


def test_imports():
    """Test that all core game imports work without errors."""
    print("🔍 Validating core game imports...")

    try:
        # Add src to path so we can import newgame modules
        project_root = Path(__file__).parent.parent
        src_path = project_root / "src"
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))

        # Test core game imports
        print("  - Testing newgame.main...")
        import newgame.main

        print("  - Testing newgame.core.game...")
        import newgame.core.game

        print("  - Testing newgame.core.game_state...")
        import newgame.core.game_state

        print("  - Testing newgame.entities.player...")
        import newgame.entities.player

        print("  - Testing newgame.entities.objects...")
        import newgame.entities.objects

        print("  - Testing newgame.entities.food...")
        import newgame.entities.food

        print("  - Testing newgame.systems.ui...")
        import newgame.systems.ui

        print("  - Testing newgame.config.settings...")
        import newgame.config.settings

        print("  - Testing newgame.config.constants...")
        import newgame.config.constants

        print("  - Testing newgame.utils.math...")
        import newgame.utils.math

        # Test pygame import
        print("  - Testing pygame...")
        import pygame

        # Verify pygame can initialize (basic functionality test)
        pygame.init()
        if not pygame.get_init():
            raise ImportError("pygame failed to initialize")
        pygame.quit()

        print("✅ All imports successful!")
        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        print("\nTroubleshooting:")
        print("  1. Ensure you're in the project root directory")
        print("  2. Activate your virtual environment:")
        print("     Windows: .\\venv\\Scripts\\Activate.ps1")
        print("     Linux/macOS: source venv/bin/activate")
        print("  3. Install dependencies: pip install -r requirements.txt")
        print("  4. If pygame fails, check system requirements for graphics/audio")
        return False

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def test_basic_instantiation():
    """Test that core game objects can be instantiated."""
    print("\n🔍 Testing basic object instantiation...")

    try:
        # Test that we can create core game objects without errors
        from newgame.core.game_state import GameStateManager
        from newgame.entities.player import Player
        from newgame.entities.objects import Lodge, Dam
        from newgame.entities.food import FoodManager
        from newgame.systems.ui import UI

        print("  - Creating GameStateManager...")
        game_state = GameStateManager()

        print("  - Creating Player...")
        player = Player(100, 100)

        print("  - Creating Lodge...")
        lodge = Lodge(50, 50)

        print("  - Creating Dam...")
        dam = Dam()

        print("  - Creating UI...")
        ui = UI()

        print("  - Creating FoodManager...")
        food_manager = FoodManager(lodge.get_collision_rect(), dam.get_collision_rect())

        print("✅ Basic instantiation successful!")
        return True

    except Exception as e:
        print(f"❌ Instantiation failed: {e}")
        return False


def main():
    """Main validation function."""
    print("🚀 Newgame Build Validation")
    print("=" * 40)

    # Test imports
    imports_ok = test_imports()

    # Only test instantiation if imports worked
    instantiation_ok = True
    if imports_ok:
        instantiation_ok = test_basic_instantiation()

    # Final result
    print("\n" + "=" * 40)
    if imports_ok and instantiation_ok:
        print("🎉 Build validation PASSED!")
        print("Your development environment is ready for the Beaver Survival Game.")
        return 0
    else:
        print("💥 Build validation FAILED!")
        print("Please fix the issues above before proceeding with development.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
