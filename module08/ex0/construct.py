import os
import sys
import site


def detect_venv(curr_dir: str, global_dir: str) -> bool:
    if curr_dir == global_dir:
        return False
    return True


def venv_welcome(venv: bool) -> str:
    if not venv:
        return "You're still plugged in"
    return "Welcome to the construct"


def get_venv_name(venv: bool) -> str | None:
    if not venv:
        return "None detected"
    return os.path.basename(os.environ.get("VIRTUAL_ENV", ""))


def global_isolated_env(venv: bool) -> str:
    if not venv:
        return ("\nWARNING: You're in the global environment!"
                "\nThe machines can see everything you install.")
    return ("\nSUCCESS: You're in an isolated environment!"
            "\nSafe to install packages without affecting"
            "\nthe global system.")


def get_instructions(venv: bool) -> str:
    if not venv:
        return ("\nTo enter the construct, run:"
                "\npython -m venv matrix_env"
                "\nsource matrix_env/bin/activate # On Unix"
                "\nmatrix_env\\Scripts\\activate # On Windows"
                "\n\nThen run this program again.")
    return ("\nPackage installation path:"
            f"{site.getsitepackages()[0]}")


def main() -> None:
    curr_dir: str = sys.prefix
    global_dir: str = sys.base_prefix
    python: str = sys.executable
    is_venv: bool = detect_venv(curr_dir, global_dir)
    venv_name: str | None = get_venv_name(is_venv)
    env_status: str = global_isolated_env(is_venv)
    print(f"\nMATRIX STATUS: {venv_welcome(is_venv)}")
    print(f"\nCurrent Python: {python}")
    print(f"Virtual Environment: {venv_name}")
    if is_venv:
        print(f"Environment Path: {curr_dir}")
    print(f"{env_status}")
    print(get_instructions(is_venv))


if __name__ == "__main__":
    main()
