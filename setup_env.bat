@echo off
REM Python Virtual Environment Setup Script for Newgame Project (Windows)
REM This script automates the creation and setup of a Python virtual environment

echo 🎮 Setting up Python virtual environment for Newgame project...

REM Check if Python 3.12 is available
where python3.12 >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON_CMD=python3.12
) else (
    where python >nul 2>&1
    if %errorlevel% == 0 (
        set PYTHON_CMD=python
        echo ⚠️  Warning: python3.12 not found, using python instead
    ) else (
        echo ❌ Error: Python is not installed or not in PATH
        echo 💡 Please install Python from https://python.org
        pause
        exit /b 1
    )
)

REM Check Python version
echo 🐍 Checking Python version...
%PYTHON_CMD% --version

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    %PYTHON_CMD% -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Failed to create virtual environment
        echo 💡 Make sure Python venv module is available
        pause
        exit /b 1
    )
) else (
    echo 📦 Virtual environment already exists
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo ⚠️  Warning: Failed to upgrade pip, continuing with installation...
)

REM Install dependencies with retry logic
echo 📚 Installing dependencies from requirements.txt...
set MAX_RETRIES=3
set RETRY_COUNT=0

:retry_loop
if %RETRY_COUNT% geq %MAX_RETRIES% goto install_failed

python -m pip install --timeout 300 --retries 2 -r requirements.txt
if %errorlevel% == 0 (
    echo ✅ Dependencies installed successfully!
    goto install_success
)

set /a RETRY_COUNT=%RETRY_COUNT%+1
if %RETRY_COUNT% lss %MAX_RETRIES% (
    echo ⚠️  Installation failed, retrying (%RETRY_COUNT%/%MAX_RETRIES%)...
    timeout /t 5 /nobreak >nul
    goto retry_loop
)

:install_failed
echo ❌ Failed to install dependencies after %MAX_RETRIES% attempts.
echo 💡 This may be due to network connectivity issues.
echo 💡 You can manually install dependencies later with:
echo    venv\Scripts\activate.bat
echo    pip install -r requirements.txt
echo.
goto setup_complete

:install_success

:setup_complete
echo ✅ Setup complete!
echo.
echo 📋 To activate the virtual environment in the future, run:
echo    venv\Scripts\activate.bat
echo.
echo 📋 To deactivate the virtual environment, run:
echo    deactivate
echo.
echo 🎮 You're now ready to start developing the Newgame project!
echo.
echo Press any key to exit...
pause >nul