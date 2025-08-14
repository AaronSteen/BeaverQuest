@echo off
REM Windows batch launcher for Newgame - Attach Mode
REM This script can be run from any directory and handles venv activation automatically.

python "%~dp0attach.py" %*