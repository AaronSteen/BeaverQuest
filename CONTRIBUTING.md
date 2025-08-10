# Contributing to Newgame

Thank you for contributing to the Beaver Survival Game! This guide will help you get started and ensure a smooth development process.

## Quick Start for Contributors

1. **Setup Environment**
   ```bash
   # Run the automated setup script
   ./setup_env.sh        # macOS/Linux
   setup_env.bat         # Windows
   ```

2. **Validate Your Environment**
   ```bash
   # Essential: Run this before starting any work
   python scripts/validate_build.py

   # Should output: "🎉 Build validation PASSED!"
   ```

3. **Make Your Changes**

4. **Test Your Changes**
   ```bash
   # Validate build still works
   python scripts/validate_build.py

   # Run existing tests
   pytest

   # Format code
   black src/ tests/

   # Check code quality
   flake8 src/ tests/
   ```

## Build Validation

The `scripts/validate_build.py` script is your first line of defense against "works on my machine" issues:

### What It Checks
- ✅ All core game module imports
- ✅ Pygame installation and initialization
- ✅ Basic object instantiation
- ✅ Virtual environment setup

### When to Run
- **Before starting development** - Ensures clean environment
- **After environment changes** - Validates setup still works
- **Before committing changes** - Catches breaking changes early
- **When debugging issues** - Isolates import/dependency problems

### Expected Output
```
🚀 Newgame Build Validation
========================================
🔍 Validating core game imports...
  - Testing newgame.main... ✅
  - Testing pygame... ✅
✅ All imports successful!

🔍 Testing basic object instantiation...
✅ Basic instantiation successful!

🎉 Build validation PASSED!
```

### If Validation Fails
The script provides specific troubleshooting guidance:
1. Activate virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Check system requirements for graphics/audio

## Development Workflow

### Recommended Process
1. Pull latest changes: `git pull origin main`
2. Create feature branch: `git checkout -b feature/your-feature`
3. **Validate environment**: `python scripts/validate_build.py` ⚠️ **IMPORTANT**
4. Make your changes
5. **Validate again**: `python scripts/validate_build.py`
6. Run tests: `pytest`
7. Format code: `black src/ tests/`
8. Commit changes: `git commit -m "Clear description"`
9. Push and create PR

### Code Quality Standards
- **Formatting**: Use `black` for consistent formatting
- **Linting**: Use `flake8` for code quality
- **Testing**: Add tests for new features
- **Validation**: All changes must pass build validation

## Common Issues

### "No module named 'pygame'"
**Solution**: Activate virtual environment and install dependencies
```bash
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

### "Import failed: newgame.core.game"
**Solution**: Ensure you're running from project root with proper environment
```bash
# From project root directory
python scripts/validate_build.py
```

### Build validation fails on fresh environment
**Solution**: Run setup script first
```bash
./setup_env.sh        # macOS/Linux
setup_env.bat         # Windows
```

## Need Help?

1. Check the build validation output for specific guidance
2. Review the [README.md](README.md) for detailed setup instructions
3. Look at existing code patterns in the `src/newgame/` directory
4. Check [Game Documentation](docs/GAME_README.md) for game mechanics

## Project Structure

```
newgame/
├── src/newgame/           # Main game package
├── scripts/               # Development tools
│   └── validate_build.py  # Build validation script
├── tests/                 # Test suite
├── docs/                  # Documentation
└── requirements.txt       # Dependencies
```

Remember: **Always run `python scripts/validate_build.py` before and after making changes!** 🚀
