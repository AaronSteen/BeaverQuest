"""
Entry point for the Beaver Survival Game.
"""

import os
import sys
import subprocess
import platform


def _check_venv_active():
    """Check if virtual environment is active."""
    # Check if running from venv Python or if VIRTUAL_ENV is set
    in_venv = (
        os.getenv("VIRTUAL_ENV") is not None
        or sys.prefix != sys.base_prefix
        or hasattr(sys, "real_prefix")
    )

    # Additional check: if running from a venv bin directory
    if sys.executable and "/venv/" in sys.executable:
        in_venv = True

    return in_venv


def _activate_venv_and_run(command_args, command_name):
    """Activate virtual environment and run the specified command."""
    if _check_venv_active():
        print(f"🎮 Launching Newgame in {command_name} mode...")
        return _run_game_with_args(command_args, command_name)

    print("🔧 Virtual environment not active. Activating...")

    # Determine platform-specific activation script
    if platform.system() == "Windows":
        activate_script = os.path.join("venv", "Scripts", "activate.bat")
        if not os.path.exists(activate_script):
            activate_script = os.path.join("venv", "Scripts", "Activate.ps1")
            shell_cmd = ["powershell", "-Command"]
        else:
            shell_cmd = ["cmd", "/c"]
    else:
        activate_script = os.path.join("venv", "bin", "activate")
        shell_cmd = ["bash", "-c"]

    if not os.path.exists(activate_script):
        print(
            "❌ Virtual environment not found. Please run setup_env.sh or setup_env.bat first."
        )
        return False

    # Create command to activate venv and run the game
    if platform.system() == "Windows":
        if "powershell" in shell_cmd:
            full_command = shell_cmd + [
                f". {activate_script}; python -m {' '.join(command_args)}"
            ]
        else:
            full_command = shell_cmd + [
                f"{activate_script} && python -m {' '.join(command_args)}"
            ]
    else:
        full_command = shell_cmd + [
            f"source {activate_script} && python -m {' '.join(command_args)}"
        ]

    try:
        print("✅ Virtual environment activated.")
        print(f"🎮 Launching Newgame in {command_name} mode...")
        subprocess.run(full_command, check=True)
        print(f"✅ Newgame {command_name} mode completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Newgame in {command_name} mode: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error launching Newgame: {e}")
        return False


def _run_game_with_args(command_args, command_name):
    """Run the game with specified module arguments."""
    try:
        subprocess.run([sys.executable, "-m"] + command_args, check=True)
        print(f"✅ Newgame {command_name} mode completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch Newgame in {command_name} mode: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error launching Newgame: {e}")
        return False


def run_game():
    """Entry point for normal game execution (run command)."""
    print("🦫 Newgame - Normal Mode")
    print("=" * 40)
    return _activate_venv_and_run(["newgame.main"], "normal")


def debug_game():
    """Entry point for debug mode with VS Code integration (debug command)."""
    print("🦫 Newgame - Debug Mode")
    print("=" * 40)
    print("🔍 Starting game with VS Code debugger integration...")
    print("💡 Make sure VS Code is ready to attach the debugger!")

    # Set environment variable for debug mode
    env = os.environ.copy()
    env["DEBUGPY_ENABLE"] = "1"

    if _check_venv_active():
        print("🎮 Launching Newgame in debug mode...")
        try:
            subprocess.run([sys.executable, "-m", "newgame.main"], env=env, check=True)
            print("✅ Newgame debug mode completed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch Newgame in debug mode: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error launching Newgame: {e}")
            return False
    else:
        print("🔧 Virtual environment not active. Activating...")

        # Platform-specific activation with debug environment
        if platform.system() == "Windows":
            activate_script = os.path.join("venv", "Scripts", "activate.bat")
            if not os.path.exists(activate_script):
                activate_script = os.path.join("venv", "Scripts", "Activate.ps1")
                shell_cmd = ["powershell", "-Command"]
            else:
                shell_cmd = ["cmd", "/c"]
        else:
            activate_script = os.path.join("venv", "bin", "activate")
            shell_cmd = ["bash", "-c"]

        if not os.path.exists(activate_script):
            print(
                "❌ Virtual environment not found. Please run setup_env.sh or setup_env.bat first."
            )
            return False

        # Create command with debug environment variable
        if platform.system() == "Windows":
            if "powershell" in shell_cmd:
                full_command = shell_cmd + [
                    f". {activate_script}; $env:DEBUGPY_ENABLE='1'; python -m newgame.main"
                ]
            else:
                full_command = shell_cmd + [
                    f"{activate_script} && set DEBUGPY_ENABLE=1 && python -m newgame.main"
                ]
        else:
            full_command = shell_cmd + [
                f"source {activate_script} && DEBUGPY_ENABLE=1 python -m newgame.main"
            ]

        try:
            print("✅ Virtual environment activated.")
            print("🎮 Launching Newgame in debug mode...")
            subprocess.run(full_command, check=True)
            print("✅ Newgame debug mode completed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch Newgame in debug mode: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error launching Newgame: {e}")
            return False


def attach_game():
    """Entry point for attach mode - game runs normally but debugger can attach (attach command)."""
    print("🦫 Newgame - Attach Mode")
    print("=" * 40)
    print("🔗 Starting game with debugger attachment capability...")
    print(
        "💡 The game will run normally. Use 'Python: Attach to Newgame Debugger' in VS Code to attach."
    )

    # Set environment variable for attach mode (same as debug but different messaging)
    env = os.environ.copy()
    env["DEBUGPY_ENABLE"] = "1"

    if _check_venv_active():
        print("🎮 Launching Newgame in attach mode...")
        try:
            subprocess.run([sys.executable, "-m", "newgame.main"], env=env, check=True)
            print("✅ Newgame attach mode completed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch Newgame in attach mode: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error launching Newgame: {e}")
            return False
    else:
        print("🔧 Virtual environment not active. Activating...")

        # Platform-specific activation with debug environment
        if platform.system() == "Windows":
            activate_script = os.path.join("venv", "Scripts", "activate.bat")
            if not os.path.exists(activate_script):
                activate_script = os.path.join("venv", "Scripts", "Activate.ps1")
                shell_cmd = ["powershell", "-Command"]
            else:
                shell_cmd = ["cmd", "/c"]
        else:
            activate_script = os.path.join("venv", "bin", "activate")
            shell_cmd = ["bash", "-c"]

        if not os.path.exists(activate_script):
            print(
                "❌ Virtual environment not found. Please run setup_env.sh or setup_env.bat first."
            )
            return False

        # Create command with debug environment variable
        if platform.system() == "Windows":
            if "powershell" in shell_cmd:
                full_command = shell_cmd + [
                    f". {activate_script}; $env:DEBUGPY_ENABLE='1'; python -m newgame.main"
                ]
            else:
                full_command = shell_cmd + [
                    f"{activate_script} && set DEBUGPY_ENABLE=1 && python -m newgame.main"
                ]
        else:
            full_command = shell_cmd + [
                f"source {activate_script} && DEBUGPY_ENABLE=1 python -m newgame.main"
            ]

        try:
            print("✅ Virtual environment activated.")
            print("🎮 Launching Newgame in attach mode...")
            subprocess.run(full_command, check=True)
            print("✅ Newgame attach mode completed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch Newgame in attach mode: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error launching Newgame: {e}")
            return False


def main():
    """Entry point for the game when called directly."""
    # Debugpy integration for debugging - placed at top as requested
    if os.getenv("DEBUGPY_ENABLE") == "1":
        import debugpy

        debugpy.listen(("localhost", 5678))  # Listen on port 5678
        print("Waiting for debugger attach...")
        debugpy.wait_for_client()  # Pause execution until VS Code attaches
        print("Debugger attached!")

    try:
        from .core.game import BeaverSurvivalGame

        game = BeaverSurvivalGame()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
