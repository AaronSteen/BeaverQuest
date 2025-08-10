# Newgame Project Hardening Test Plan

## Overview
This document outlines the implementation plan for hardening the Newgame project against "works on my machine" issues. Each section contains actionable tasks that can be implemented incrementally.

**Priority Order**: Tasks are numbered by implementation priority (P1 = highest priority)

**🚀 QUICK WINS**: Look for tasks marked with `🚀 QUICK-WIN-#` for immediate implementation with minimal setup cost.

---

## 🚀 IMMEDIATE ACTION: Quick Wins for Local Build Validation

*These tasks provide immediate "build still works" validation for topic branches with minimal infrastructure setup.*

### 🚀 QUICK-WIN-1: Basic Import Validation Script ✅ **COMPLETED**
**Estimated Time**: 30 minutes
**Dependencies**: None
**Run Time**: <5 seconds

**Tasks**:
- [x] Create `scripts/validate_build.py` that imports all core game modules
- [x] Verify all `src/newgame/` imports work without errors
- [x] Add pygame import verification
- [x] Include clear success/failure messages
- [x] Make script runnable from project root

**Implementation**:
```python
#!/usr/bin/env python3
"""Quick smoke test - verify all core imports work"""
import sys
from pathlib import Path

def test_imports():
    try:
        # Test core game imports
        import newgame.main
        import newgame.core.game
        import newgame.entities.player
        import newgame.systems.ui
        # Test pygame
        import pygame
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if test_imports() else 1)
```

**Usage**: `python scripts/validate_build.py`

**✅ COMPLETION NOTES**:
- **Implemented**: `scripts/validate_build.py` with comprehensive import testing
- **Features Added**: Enhanced error reporting, basic object instantiation testing, clear success/failure messages
- **Documentation**: Added to README.md, CONTRIBUTING.md, and copilot instructions
- **Tested**: Successfully validates all core imports and pygame functionality
- **Runtime**: ~5 seconds, meets performance target

### 🚀 QUICK-WIN-2: Game Initialization Test ✅ **COMPLETED**
**Estimated Time**: 1 hour
**Dependencies**: QUICK-WIN-1 ✅
**Run Time**: <10 seconds

**Tasks**:
- [x] Create `tests/test_smoke.py` for basic game initialization
- [x] Test pygame can initialize (headless mode)
- [x] Test game can create main game object
- [x] Verify player object can be instantiated
- [x] Add to existing pytest suite

**Implementation**:
```python
"""Smoke tests - verify game can initialize without crashing"""
import pygame
import pytest

def test_pygame_init():
    """Test pygame initializes without errors"""
    pygame.init()
    assert pygame.get_init()
    pygame.quit()

def test_game_creation():
    """Test main game object can be created"""
    from newgame.core.game import Game
    game = Game()
    assert game is not None

def test_player_creation():
    """Test player object can be instantiated"""
    from newgame.entities.player import Player
    player = Player()
    assert player is not None
```

**Usage**: `python -m pytest tests/test_smoke.py -v`

**✅ COMPLETION NOTES**:
- **Implemented**: `tests/test_smoke.py` with 10 comprehensive initialization tests
- **Features Added**:
  - Pygame initialization/cleanup testing (headless safe)
  - Full game object creation validation
  - Component instantiation testing (Player, Lodge, Dam, UI, FoodManager)
  - Configuration import validation
  - Complete game initialization flow testing
- **Integration**: Seamlessly added to existing pytest suite (now 20 total tests)
- **Performance**: ~3 seconds runtime, well under 10-second target
- **Coverage**: Tests cover all major game systems and catch initialization failures

### 🚀 QUICK-WIN-3: Enhanced Setup Script Validation 🟡 **BLOCKED**
**Estimated Time**: 1-2 hours
**Dependencies**: QUICK-WIN-1 ✅
**Run Time**: <15 seconds

**Tasks**:
- [ ] Enhance existing `setup_env.bat` with basic validation
- [ ] Add Python version check (3.12.x)
- [ ] Add pygame import verification
- [ ] Add virtual environment activation check
- [ ] Provide clear error messages with fix suggestions

**Enhancement to add to `setup_env.bat`**:
```batch
REM Add validation section at end of setup_env.bat
echo Validating installation...
python -c "import sys; assert sys.version_info >= (3, 12), f'Need Python 3.12+, got {sys.version}'"
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python version check failed
    exit /b 1
)

python -c "import pygame; print('✅ pygame available')"
if %ERRORLEVEL% NEQ 0 (
    echo ❌ pygame not available
    exit /b 1
)

python scripts/validate_build.py
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Build validation failed
    exit /b 1
)

echo ✅ Environment setup and validation complete!
```

### 🚀 QUICK-WIN-4: Basic Pre-commit Hook � **READY**
**Estimated Time**: 1 hour
**Dependencies**: QUICK-WIN-1 ✅, QUICK-WIN-2 ✅
**Run Time**: <20 seconds

**Tasks**:
- [ ] Install `pre-commit` package in requirements.txt
- [ ] Create `.pre-commit-config.yaml` with essential checks
- [ ] Configure black code formatting check
- [ ] Configure flake8 linting
- [ ] Add basic import validation hook
- [ ] Document installation for team

**Implementation** (`.pre-commit-config.yaml`):
```yaml
repos:
- repo: https://github.com/psf/black
  rev: 23.3.0
  hooks:
  - id: black
    language_version: python3.12

- repo: https://github.com/pycqa/flake8
  rev: 6.0.0
  hooks:
  - id: flake8
    args: [--max-line-length=88]

- repo: local
  hooks:
  - id: validate-build
    name: Validate Build
    entry: python scripts/validate_build.py
    language: system
    always_run: true

- repo: local
  hooks:
  - id: smoke-tests
    name: Smoke Tests
    entry: python -m pytest tests/test_smoke.py -v
    language: system
    always_run: true
```

**Setup**: `pre-commit install` (run once per developer)

---

## 1. Continuous Integration Pipeline (P1)

### 1.1 Basic GitHub Actions Setup
**Estimated Time**: 4-6 hours
**Dependencies**: None

**Tasks**:
- [ ] Create `.github/workflows/ci.yml` with basic Python setup
- [ ] Configure matrix testing for Python 3.12 on Windows, macOS, Linux
- [ ] Add step to activate virtual environment using setup scripts
- [ ] Add step to run existing tests (`pytest`)
- [ ] Add step to run code quality checks (`black --check`, `flake8`)

**Acceptance Criteria**:
- CI runs on all three platforms
- All existing tests pass
- Code quality checks pass
- Build fails if any step fails

### 1.2 Game Functionality Verification in CI
**Estimated Time**: 2-3 hours
**Dependencies**: 1.1

**Tasks**:
- [ ] Add pygame import test to CI (verify pygame installs correctly)
- [ ] Create headless game initialization test
- [ ] Add test that verifies game can reach main menu state
- [ ] Configure virtual display for Linux CI (xvfb)

**Acceptance Criteria**:
- CI can import pygame without errors
- Game initializes without crashing
- Main game loop can start (even if headless)

---

## 2. Enhanced Testing Strategy (P1)

### 2.1 Integration Test Suite
**Estimated Time**: 6-8 hours
**Dependencies**: None

**Tasks**:
- [ ] Create `tests/integration/` directory
- [ ] Write `test_game_initialization.py` - verifies pygame setup, window creation
- [ ] Write `test_player_creation.py` - verifies player entity creation and basic properties
- [ ] Write `test_screen_transitions.py` - verifies movement between game screens
- [ ] Write `test_food_collection.py` - verifies food collection mechanics
- [ ] Write `test_game_state_persistence.py` - verifies game state management

**Acceptance Criteria**:
- All integration tests run in under 30 seconds
- Tests can run headless (for CI)
- Tests verify actual game functionality, not just imports

### 2.2 Cross-Platform Compatibility Tests
**Estimated Time**: 4-5 hours
**Dependencies**: 2.1

**Tasks**:
- [ ] Create `tests/platform/` directory
- [ ] Write `test_file_paths.py` - verify path handling works on Windows/Unix
- [ ] Write `test_asset_loading.py` - verify all game assets load correctly
- [ ] Write `test_display_modes.py` - verify pygame display works across platforms
- [ ] Write `test_input_handling.py` - verify keyboard input works consistently

**Acceptance Criteria**:
- Tests pass on Windows, macOS, and Linux
- File operations work with both forward and backslashes
- All game assets load without path errors

### 2.3 Performance Regression Tests
**Estimated Time**: 3-4 hours
**Dependencies**: 2.1

**Tasks**:
- [ ] Create `tests/performance/` directory
- [ ] Write `test_frame_rate.py` - measure and verify minimum FPS
- [ ] Write `test_memory_usage.py` - monitor memory consumption over time
- [ ] Write `test_startup_time.py` - verify game starts within reasonable time
- [ ] Create performance baseline measurements file

**Acceptance Criteria**:
- Game maintains 60 FPS minimum during normal gameplay
- Memory usage stays under defined thresholds
- Game starts within 3 seconds on modern hardware

---

## 3. Environment Validation (P2)

### 3.1 Enhanced Setup Script Validation
**Estimated Time**: 3-4 hours
**Dependencies**: None

**Tasks**:
- [ ] Modify `setup_env.bat` to include pygame validation
- [ ] Modify `setup_env.sh` to include pygame validation
- [ ] Add display capability check (resolution, color depth)
- [ ] Add audio system validation
- [ ] Create `validate_environment.py` script for comprehensive checks
- [ ] Add error reporting with specific fix suggestions

**Acceptance Criteria**:
- Setup scripts verify pygame can initialize
- Scripts detect and report missing system dependencies
- Clear error messages with actionable fix instructions
- Validation script can run independently

### 3.2 System Requirements Documentation
**Estimated Time**: 2-3 hours
**Dependencies**: 3.1

**Tasks**:
- [ ] Document minimum system requirements (Python version, OS versions)
- [ ] Document required system libraries (SDL, audio drivers)
- [ ] Create troubleshooting guide for common setup issues
- [ ] Document graphics requirements (minimum resolution, color depth)
- [ ] Create platform-specific setup notes

**Acceptance Criteria**:
- Clear requirements documentation
- Troubleshooting guide covers common issues
- Platform-specific instructions are accurate

---

## 4. Pre-commit Hooks (P2)

### 4.1 Git Hooks Setup
**Estimated Time**: 2-3 hours
**Dependencies**: None

**Tasks**:
- [ ] Install and configure `pre-commit` package
- [ ] Create `.pre-commit-config.yaml` with black, flake8, and basic tests
- [ ] Add custom hook for game import validation
- [ ] Add hook to verify no debug print statements
- [ ] Create setup instructions for team members

**Acceptance Criteria**:
- Hooks run automatically on commit
- Code formatting is enforced
- Basic game functionality is verified before commit
- Hooks can be bypassed in emergency (with warning)

### 4.2 Custom Game Validation Hooks
**Estimated Time**: 3-4 hours
**Dependencies**: 4.1

**Tasks**:
- [ ] Create hook script that verifies game imports work
- [ ] Add hook to check that all required assets exist
- [ ] Create hook to verify configuration files are valid
- [ ] Add hook to run quick smoke tests
- [ ] Document hook customization for team

**Acceptance Criteria**:
- Custom hooks run in under 10 seconds
- Hooks catch common breaking changes
- Team can easily add new validation rules

---

## 5. Dependency Management (P3)

### 5.1 Migration to pyproject.toml
**Estimated Time**: 2-3 hours
**Dependencies**: None

**Tasks**:
- [ ] Migrate from `requirements.txt` to `pyproject.toml`
- [ ] Configure build system (setuptools/poetry)
- [ ] Separate dev, test, and runtime dependencies
- [ ] Pin all transitive dependencies
- [ ] Update setup scripts to use new dependency management

**Acceptance Criteria**:
- All dependencies are locked with exact versions
- Development and runtime dependencies are separate
- Setup scripts work with new dependency format
- Build system is properly configured

### 5.2 Dependency Security and Updates
**Estimated Time**: 2-3 hours
**Dependencies**: 5.1

**Tasks**:
- [ ] Add dependency vulnerability scanning
- [ ] Create automated dependency update workflow
- [ ] Document dependency update process
- [ ] Set up automated security alerts
- [ ] Create dependency review checklist

**Acceptance Criteria**:
- Security vulnerabilities are detected automatically
- Process exists for safe dependency updates
- Team is notified of security issues

---

## 6. Game-Specific Validation (P3)

### 6.1 Asset Management Testing
**Estimated Time**: 4-5 hours
**Dependencies**: 2.1

**Tasks**:
- [ ] Create inventory of all required game assets
- [ ] Write tests to verify all sprites load correctly
- [ ] Write tests to verify all sounds load correctly
- [ ] Create asset validation script for CI
- [ ] Add missing asset detection with clear error messages

**Acceptance Criteria**:
- All game assets are catalogued
- Missing assets cause immediate, clear failures
- Asset loading is tested across platforms

### 6.2 Game State Validation
**Estimated Time**: 5-6 hours
**Dependencies**: 2.1

**Tasks**:
- [ ] Write tests for game state transitions (menu -> game -> pause)
- [ ] Write tests for player state persistence
- [ ] Write tests for food collection and storage mechanics
- [ ] Write tests for coordinate system and movement
- [ ] Create game state debugging tools

**Acceptance Criteria**:
- All major game states are tested
- State transitions work correctly
- Game mechanics behave consistently

---

## 7. Documentation and Onboarding (P4)

### 7.1 Developer Setup Documentation
**Estimated Time**: 3-4 hours
**Dependencies**: 3.1, 4.1

**Tasks**:
- [ ] Create comprehensive setup guide for new developers
- [ ] Document common development workflows
- [ ] Create troubleshooting FAQ
- [ ] Document testing procedures
- [ ] Create contribution guidelines

**Acceptance Criteria**:
- New developer can set up environment in under 30 minutes
- Common issues are documented with solutions
- Clear guidelines for contributing code

### 7.2 Architecture Documentation
**Estimated Time**: 4-5 hours
**Dependencies**: None

**Tasks**:
- [ ] Document current game architecture
- [ ] Create module dependency diagram
- [ ] Document design patterns used
- [ ] Create guidelines for making changes
- [ ] Document testing strategy

**Acceptance Criteria**:
- Architecture is clearly documented
- Design decisions are explained
- Guidelines prevent breaking changes

---

## 8. Build and Distribution (P5)

### 8.1 Automated Packaging
**Estimated Time**: 6-8 hours
**Dependencies**: 1.1, 5.1

**Tasks**:
- [ ] Research and select packaging tool (PyInstaller vs cx_Freeze)
- [ ] Create packaging configuration
- [ ] Add packaging step to CI pipeline
- [ ] Test packaged game on clean systems
- [ ] Create distribution workflow

**Acceptance Criteria**:
- Game can be packaged into standalone executable
- Packaged game runs on systems without Python
- Packaging is automated in CI

### 8.2 Release Process
**Estimated Time**: 3-4 hours
**Dependencies**: 8.1

**Tasks**:
- [ ] Create release checklist
- [ ] Automate version bumping
- [ ] Create release notes template
- [ ] Set up automated release creation
- [ ] Document release process

**Acceptance Criteria**:
- Releases are created consistently
- Release process is documented
- Version management is automated

---

## Implementation Schedule

### 🚀 IMMEDIATE (Days 1-2): Quick Wins - Start Here!
- Complete 🚀 QUICK-WIN-1: Basic Import Validation (30 min)
- Complete 🚀 QUICK-WIN-2: Game Initialization Test (1 hour)
- Complete 🚀 QUICK-WIN-3: Enhanced Setup Validation (1-2 hours)
- Complete 🚀 QUICK-WIN-4: Basic Pre-commit Hook (1 hour)

**Total Time Investment**: 3.5-4.5 hours
**Impact**: Catches 80% of common breaking changes locally

### Phase 1 (Weeks 1-2): Foundation
- Complete items 1.1, 1.2 (CI Pipeline)
- Complete items 2.1, 2.2 (Core Testing)
- Complete items 3.1 (Environment Validation)

### Phase 2 (Weeks 3-4): Quality Assurance
- Complete items 4.1, 4.2 (Pre-commit Hooks)
- Complete items 2.3 (Performance Testing)
- Complete items 5.1 (Dependency Management)

### Phase 3 (Weeks 5-6): Game Validation
- Complete items 6.1, 6.2 (Game-Specific Tests)
- Complete items 7.1, 7.2 (Documentation)

### Phase 4 (Weeks 7-8): Distribution
- Complete items 8.1, 8.2 (Build and Release)
- Complete items 5.2 (Security)

---

## Success Metrics

### Technical Metrics
- [ ] CI pipeline has <5% false positive failure rate
- [ ] Test suite runs in under 2 minutes
- [ ] 100% of commits pass pre-commit hooks
- [ ] Game starts successfully on 3 major platforms
- [ ] Zero missing asset failures in production

### Process Metrics
- [ ] New developer setup time < 30 minutes
- [ ] Average time to resolve "works on my machine" issues < 1 hour
- [ ] 100% of releases pass all automated tests
- [ ] Team confidence in deployment process > 95%

## Risk Mitigation

### High-Risk Areas
- **Pygame platform differences**: Extensive cross-platform testing required
- **CI/CD complexity**: Start simple, iterate
- **Performance regression**: Establish baselines early
- **Team adoption**: Provide clear documentation and training

### Mitigation Strategies
- Implement incrementally, test each phase thoroughly
- Maintain backward compatibility during transitions
- Provide rollback plans for each major change
- Get team buy-in before implementing process changes
