#!/usr/bin/env python3
"""
Cross-platform launcher for Newgame - Attach Mode
This script can be run from any directory and handles venv activation automatically.
"""
import os
import sys
import subprocess
import platform


def find_project_root():
    """Find the project root directory containing pyproject.toml."""
    current = os.path.abspath(os.path.dirname(__file__))
    while current != os.path.dirname(current):  # Not root
        if os.path.exists(os.path.join(current, 'pyproject.toml')):
            return current
        current = os.path.dirname(current)
    return None


def check_venv_active():
    """Check if virtual environment is active."""
    return (
        os.getenv("VIRTUAL_ENV") is not None
        or sys.prefix != sys.base_prefix
        or hasattr(sys, "real_prefix")
    )


def activate_venv_and_run():
    """Activate virtual environment and run the game in attach mode."""
    project_root = find_project_root()
    if not project_root:
        print("❌ Could not find project root (pyproject.toml not found)")
        sys.exit(1)
    
    os.chdir(project_root)
    
    print("🦫 Newgame - Attach Mode")
    print("=" * 40)
    print("🔗 Starting game with debugger attachment capability...")
    print("💡 The game will run normally. Use 'Python: Attach to Newgame Debugger' in VS Code to attach.")
    
    if check_venv_active():
        print("🎮 Launching Newgame in attach mode...")
        env = os.environ.copy()
        env["DEBUGPY_ENABLE"] = "1"
        try:
            subprocess.run([sys.executable, "-m", "newgame.main"], env=env, check=True)
            print("✅ Newgame attach mode completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch Newgame in attach mode: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            sys.exit(1)
        return

    print("🔧 Virtual environment not active. Activating...")

    # Find activation script
    if platform.system() == "Windows":
        activate_script = os.path.join("venv", "Scripts", "activate.bat")
        powershell_script = os.path.join("venv", "Scripts", "Activate.ps1")
        
        if os.path.exists(powershell_script):
            shell_cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-Command"]
            full_command = shell_cmd + [
                f"& '{powershell_script}'; $env:DEBUGPY_ENABLE='1'; python -m newgame.main"
            ]
        elif os.path.exists(activate_script):
            shell_cmd = ["cmd", "/c"]
            full_command = shell_cmd + [
                f'"{activate_script}" && set DEBUGPY_ENABLE=1 && python -m newgame.main'
            ]
        else:
            print("❌ Virtual environment not found. Please run setup_env.bat first.")
            sys.exit(1)
    else:
        activate_script = os.path.join("venv", "bin", "activate")
        if not os.path.exists(activate_script):
            print("❌ Virtual environment not found. Please run ./setup_env.sh first.")
            sys.exit(1)
        
        shell_cmd = ["bash", "-c"]
        full_command = shell_cmd + [
            f"source '{activate_script}' && DEBUGPY_ENABLE=1 python -m newgame.main"
        ]

    try:
        print("✅ Virtual environment activated.")
        print("🎮 Launching Newgame in attach mode...")
        subprocess.run(full_command, check=True, cwd=project_root)
        print("✅ Newgame attach mode completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Newgame in attach mode: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    activate_venv_and_run()