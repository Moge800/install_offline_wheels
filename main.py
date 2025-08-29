import os
from pathlib import Path


def check_venv_system() -> bool:
    """Check if the current Python environment is a virtual environment.

    Returns:
        bool: True if running in a virtual environment, False otherwise.
    """
    import sys

    # Method 1: Check for VIRTUAL_ENV environment variable
    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        return True

    # Method 2: Check if sys.prefix differs from sys.base_prefix
    # In a virtual environment, these will be different
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        return True

    # Method 3: Check for common virtual environment indicators
    # Check if running from Scripts/bin directory typical of venv
    executable_path = Path(sys.executable)
    parent_names = [p.name.lower() for p in executable_path.parents]

    if any(name in ["scripts", "bin"] for name in parent_names):
        # Additional check: look for pyvenv.cfg file which indicates a venv
        for parent in executable_path.parents:
            if (parent / "pyvenv.cfg").exists():
                return True

    return False


def decorate_function(func):
    def wrapper(*args, **kwargs):
        if check_venv_system():
            print("Running in a virtual environment.")
        else:
            print("Not running in a virtual environment.")
            if input("Are you serious?(y/n)>") == "y":
                print("Proceeding without a virtual environment.")
            else:
                print("Aborting.")
                return None
        return func(*args, **kwargs)

    return wrapper


def wheel_directory_exists(wheel_dir: Path) -> bool:
    return wheel_dir.exists() and wheel_dir.is_dir()


def get_wheel_files(wheel_dir: Path) -> list[Path]:
    return [f for f in wheel_dir.iterdir() if f.is_file() and f.name.endswith(".whl")]


def get_wheel_file_paths(wheel_dir: Path) -> list[Path]:
    return [f for f in get_wheel_files(wheel_dir)]


def install_wheel(wheel_path_list: list[Path]) -> None:
    wheel_path = " ".join(str(p) for p in wheel_path_list)
    os.system(f"pip install {wheel_path} --no-deps --force-reinstall")


@decorate_function
def main():
    wheel_dir = Path("./downloads/")
    if wheel_directory_exists(wheel_dir):
        wheel_files = get_wheel_file_paths(wheel_dir)
        if wheel_files:
            install_wheel(wheel_files)
        else:
            print("No wheel files found.")
    else:
        print("Wheel directory does not exist.")


if __name__ == "__main__":
    main()
