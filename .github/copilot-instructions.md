# LLM/Agent Instructions for Newgame Project

## Project Overview
This is **Newgame**, a 2D top-down adventure game where you play as a beaver collecting resources from woodland areas to avoid dying. The game is visually inspired by Zelda: Link to the Past and is built with Python using pygame.

### Key Game Concepts
- **Game World**: 9x9 coordinate plane (zero-indexed), starting at HOME_SCREEN [4,4]
- **HOME_SCREEN**: Contains the beaver's lodge (safe zone) and a dam along the north border
- **Goal**: Collect food resources to maintain food storage and survive
- **Food Mechanics**: Storage starts at 120, decreases by 1 every 4 seconds, increases by 5 when collecting food items
- **Controls**: WASD/Arrow keys (movement), Space (bite), Esc (pause menu)

## Development Environment

### Python Environment Setup
- **Required Python Version**: 3.12.3 (specified in `.python-version`)
- **Virtual Environment**: Always use the `venv` folder for isolation
- **Dependencies**: Managed via `requirements.txt` (pygame, pytest, black, flake8, etc.)

### Platform-Specific Setup Scripts
**ALWAYS use the automated setup scripts before working with this project:**

#### Windows (Current Environment):
```cmd
setup_env.bat
```

#### macOS/Linux:
```bash
./setup_env.sh
```

These scripts handle:
- Python version detection (prefers 3.12, falls back gracefully)
- Virtual environment creation/validation
- Dependency installation with retry logic
- Environment activation guidance

**When attempting to run the game, ensure the virtual environment is activated!**
- e.g. if a command like `python src/newgame/main.py` fails, retry by running `.\venv\Scripts\Activate.ps1 && python src/newgame/main.py` (or `source venv/bin/activate && python src/newgame/main.py` on macOS/Linux.)

### Manual Environment Activation
After initial setup, activate the environment:

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

## Project Structure
```
newgame/
├── .python-version      # Python 3.12.3 requirement
├── requirements.txt     # pygame, testing, and dev tools
├── setup_env.bat       # Windows environment setup
├── setup_env.sh        # macOS/Linux environment setup
├── design_doc.md       # Game design specifications
├── examples/           # Demo and verification code
│   └── game_example.py # pygame setup verification
├── copilot.md          # This file
└── README.md           # Project documentation
```

## Development Workflow Guidelines

### Before Making Changes
1. **ALWAYS** ensure the virtual environment is active
2. **ALWAYS** run the appropriate setup script if working on a new machine
3. **VALIDATE** your environment: `python scripts/validate_build.py`
4. **VERIFY** pygame installation by running: `python examples/game_example.py`

### Build Validation
- **Quick Test**: `python scripts/validate_build.py` - Validates all imports and basic functionality
- **Runtime**: ~5 seconds
- **Purpose**: Catches "works on my machine" issues early in development
- **When to Use**: Before development work, after environment changes, before commits

### Code Quality Standards
- **Formatting**: Use `black .` for consistent code formatting
- **Linting**: Use `flake8 .` for code quality checks
- **Testing**: Use `pytest` for running tests (when available)

### Dependencies to Be Aware Of
- **pygame**: Core game engine and graphics
- **pytest/pytest-cov**: Testing framework and coverage
- **black**: Code formatting (run before commits)
- **flake8**: Linting and code quality
- **Sphinx**: Documentation generation

### Key Files to Reference
- `design_doc.md`: Complete game design specifications and mechanics
- `README.md`: Detailed setup instructions and troubleshooting
- `requirements.txt`: All Python dependencies with versions

### Common Tasks
1. **New Feature Development**: Check design_doc.md for specifications
2. **Environment Issues**: Run appropriate setup script, check README troubleshooting
3. **Testing**: Ensure pygame imports work with the verification script
4. **Code Quality**: Run black and flake8 before submitting changes

### Important Notes
- The project uses the py launcher on Windows for Python version management
- Virtual environment is essential - never install packages globally
- Setup scripts have robust error handling and retry logic
- Game coordinates use zero-indexing with [0,0] at northwest corner

Remember: This is a beaver adventure game with specific gameplay mechanics around food storage and survival. Always consider the game design context when implementing features.

