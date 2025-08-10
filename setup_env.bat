@echo off
setlocal EnableExtensions EnableDelayedExpansion

echo [STEP 0] Starting Python venv setup for Newgame...
echo [INFO ] Current dir: %CD%

REM --- Step 1: Detect Python interpreter (prefer py launcher) ---
echo [STEP 1] Detecting Python interpreter...
set "PY_CMD="
py -3.12 -V >nul 2>&1 & if !errorlevel!==0 set "PY_CMD=py -3.12"
if not defined PY_CMD (
    py -3 -V >nul 2>&1 & if !errorlevel!==0 set "PY_CMD=py -3"
)
if not defined PY_CMD (
    python -V >nul 2>&1 & if !errorlevel!==0 set "PY_CMD=python"
)
if not defined PY_CMD (
    echo [ERROR] No suitable Python found via py/python. Using WHERE to probe...
    where py
    where python
    exit /b 1
)
echo [INFO ] Using interpreter: %PY_CMD%
for /f "delims=" %%V in ('%PY_CMD% --version 2^>^&1') do echo   %%V

REM --- Step 2: Create venv if missing ---
echo [STEP 2] Checking virtual environment folder...
if not exist "venv" (
    echo   venv not found, creating...
    %PY_CMD% -m venv venv
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to create virtual environment.
        exit /b 1
    )
) else (
    echo   venv already exists.
)

REM --- Step 3: Point directly to venv python ---
set "VENV_PY=%CD%\venv\Scripts\python.exe"
if not exist "%VENV_PY%" (
    echo [ERROR] venv\Scripts\python.exe not found. Contents of venv\Scripts:
    dir /b "venv\Scripts"
    echo pyvenv.cfg:
    type "venv\pyvenv.cfg" 2>nul
    exit /b 1
)
echo [STEP 3] Using venv interpreter: "%VENV_PY%"
"%VENV_PY%" --version

REM --- Step 4: Upgrade pip inside venv ---
echo [STEP 4] Upgrading pip in venv...
"%VENV_PY%" -m pip install --upgrade pip
if !errorlevel! neq 0 (
    echo [WARN ] Could not upgrade pip; continuing.
) else (
    echo   pip upgraded successfully.
)

REM --- Step 5: Install dependencies (with delayed expansion) ---
echo [STEP 5] Checking for requirements.txt...
if exist requirements.txt (
    echo   Found requirements.txt, installing dependencies...
    set "MAX_RETRIES=3"
    set "RETRY_COUNT=0"

:retry_loop
    echo   Attempt !RETRY_COUNT! of !MAX_RETRIES!...
    "%VENV_PY%" -m pip install --timeout 300 --retries 2 -r requirements.txt
    if !errorlevel!==0 (
        echo   Dependencies installed successfully.
        goto install_success
    )

    set /a RETRY_COUNT+=1
    if !RETRY_COUNT! lss !MAX_RETRIES! (
        echo   Install failed, retrying in 5 seconds...
        timeout /t 5 /nobreak >nul
        goto retry_loop
    )

    echo [ERROR] Failed to install dependencies after !MAX_RETRIES! attempts.
) else (
    echo   No requirements.txt found. Skipping dependency installation.
)

:install_success

REM --- Step 6: Best-effort activation (optional) ---
echo [STEP 6] Attempting to activate venv (cmd.exe)...
if exist "venv\Scripts\activate.bat" (
    call "venv\Scripts\activate.bat"
    if !errorlevel!==0 (
        echo   venv activated. Current python:
        python --version
    ) else (
        echo [WARN ] Activation script returned non-zero. Continuing without activation.
    )
) else (
    echo [INFO ] activate.bat not found. In PowerShell use:
    echo        .\venv\Scripts\Activate.ps1
)

REM --- Step 7: Wrap up ---
echo [STEP 7] Setup complete.
echo.
echo To use the venv in this shell (cmd.exe):
echo    call venv\Scripts\activate.bat
echo In PowerShell:
echo    .\venv\Scripts\Activate.ps1
echo.
echo To run without activating:
echo    "%VENV_PY%" -m pip list
echo    "%VENV_PY%" your_script.py
echo.

endlocal
