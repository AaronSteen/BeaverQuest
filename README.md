# Newgame - Beaver Adventure Game

A 2D top-down adventure game where you play as a beaver collecting resources from the surrounding woodland, with the goal of avoiding dying. Visually inspired by Zelda: Link to the Past.

## Game Overview

- **Genre**: 2D Top-down Adventure
- **Setting**: Woodland environment with a beaver protagonist
- **World**: 9x9 coordinate plane with the player starting at the center (4,4)
- **Starting Area**: Player's lodge with a dam along the north border

## Development Environment Setup

This project uses Python for game development with pygame as the main game engine. Follow these steps to set up a consistent development environment across different machines.

### Prerequisites

- Python 3.12.3 (recommended version specified in `.python-version`)
- Git (for version control)

### Quick Setup (Recommended)

The easiest way to set up your development environment is to use the automated setup script:

#### On macOS/Linux:
```bash
# Clone the repository (if you haven't already)
git clone https://github.com/friendlyman23/newgame.git
cd newgame

# Run the setup script
./setup_env.sh
```

#### On Windows:
```cmd
# Clone the repository (if you haven't already)
git clone https://github.com/friendlyman23/newgame.git
cd newgame

# Run the setup script
setup_env.bat
```

This script will:
- Create a Python virtual environment
- Install all required dependencies
- Activate the environment for immediate use

### Manual Setup

If you prefer to set up the environment manually:

1. **Create a virtual environment:**
   ```bash
   python3.12 -m venv venv
   ```

2. **Activate the virtual environment:**
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Python Version Management

This project specifies Python 3.12.3 in the `.python-version` file. If you're using pyenv:

```bash
# Install the specified Python version
pyenv install 3.12.3

# Set it as the local version for this project
pyenv local 3.12.3
```

### Dependencies

The project includes the following main dependencies (see `requirements.txt` for specific versions):

- **pygame**: Main game development framework
- **pytest**: Testing framework
- **pytest-cov**: Test coverage reporting
- **black**: Code formatting
- **flake8**: Code linting
- **Sphinx**: Documentation generation

### Development Workflow

1. **Activate your virtual environment** (if not already active):
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate.bat
   ```

2. **Run tests** (when available):
   ```bash
   pytest
   ```

3. **Format code**:
   ```bash
   black .
   ```

4. **Lint code**:
   ```bash
   flake8 .
   ```

5. **Deactivate environment** when done:
   ```bash
   deactivate
   ```

### Troubleshooting

#### Virtual Environment Issues

- **On macOS/Linux**: If you get permission errors, ensure the setup script is executable: `chmod +x setup_env.sh`
- **On Windows**: Run the Command Prompt as Administrator if you encounter permission issues
- If Python 3.12 isn't available, the script will fall back to `python3` (macOS/Linux) or `python` (Windows)
- Make sure you're in the project root directory when running setup commands

#### Dependency Issues

- If installation fails, try upgrading pip: `pip install --upgrade pip`
- For pygame installation issues on Linux, you may need system dependencies: `sudo apt-get install python3-dev python3-pygame`
- **On Windows**: If you encounter pygame installation issues, make sure you have the latest Visual C++ Redistributable installed
- If you encounter network timeouts during pip install, try:
  - Run the setup script again (both scripts have retry logic)
  - **macOS/Linux**: Manually install dependencies: `source venv/bin/activate && pip install -r requirements.txt`
  - **Windows**: Manually install dependencies: `venv\Scripts\activate.bat && pip install -r requirements.txt`
  - Use a different pip index: `pip install -i https://pypi.org/simple/ -r requirements.txt`

### Contributing

1. Ensure your virtual environment is set up and activated
2. Install all dependencies including development tools
3. Run tests and linting before submitting changes
4. Follow the existing code style (use `black` for formatting)

### Project Structure

```
newgame/
├── .python-version      # Specifies Python version
├── requirements.txt     # Python dependencies
├── setup_env.sh        # Environment setup script (macOS/Linux)
├── setup_env.bat       # Environment setup script (Windows)
├── design_doc.md       # Game design documentation
├── examples/           # Example code and demos
│   └── game_example.py # Simple pygame verification script
├── .gitignore          # Git ignore patterns
└── README.md           # This file
```

### Testing Your Setup

After running the setup script, you can test that everything works correctly:

```bash
# On macOS/Linux:
# Activate the virtual environment
source venv/bin/activate

# Run the example script to verify pygame works
python examples/game_example.py
```

```cmd
# On Windows:
# Activate the virtual environment
venv\Scripts\activate.bat

# Run the example script to verify pygame works
python examples/game_example.py
```

This will verify that pygame is properly installed and ready for game development.

## License

This project is currently in development. License information will be added as the project progresses.