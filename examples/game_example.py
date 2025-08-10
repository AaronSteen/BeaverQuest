#!/usr/bin/env python3
"""
Example game file to demonstrate the development environment setup.
This is a minimal pygame example that can be used to verify the environment works.

To run this example (once pygame is installed):
    source venv/bin/activate
    python examples/game_example.py
"""

def main():
    """Simple example to verify pygame setup."""
    try:
        import pygame
        print("🎮 Pygame successfully imported!")
        print(f"🐍 Using Python with pygame {pygame.version.ver}")
        print("✅ Environment setup is working correctly!")
        print("")
        print("🦫 Ready to start developing the Beaver Adventure Game!")
        print("📍 Game world: 9x9 coordinate system")
        print("🏠 Starting position: Lodge at coordinate (4,4)")
        print("🌊 Northern border: Dam blocking access to north")
        
        # Initialize pygame (this will work if everything is installed correctly)
        pygame.init()
        print("🎯 Pygame initialized successfully!")
        pygame.quit()
        
    except ImportError as e:
        print(f"❌ Pygame not available: {e}")
        print("💡 Run: source venv/bin/activate && pip install -r requirements.txt")
        return 1
    except Exception as e:
        print(f"❌ Error testing pygame: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())