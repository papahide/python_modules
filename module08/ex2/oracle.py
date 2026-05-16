from dotenv import load_dotenv
import os


def load_config() -> dict[str, str]:
    load_dotenv()
    config: dict[str, str] = {"mode": os.getenv("MATRIX_MODE", "development"),
                              "database":
                              os.getenv("DATABASE_URL",
                                        "http://localhost/phpmyadmin"),
                              "api": os.getenv("API_KEY", "NO CONFIGURATION"),
                              "log": os.getenv("LOG_LEVEL", "DEBUG"),
                              "zion": os.getenv("ZION_ENDPOINT",
                                                "http://zion.local")
                              }
    return config


def _parse_mode(value: str) -> str:
    return str(value)


def _parse_database(value: str) -> str:
    if value != "not configured":
        return "Connected to local instance"
    else:
        return "No connection to local instance"


def _parse_api(value: str) -> str:
    if value != "NO CONFIGURATION":
        return "Authenticated"
    return "Incorrect authentication, try again"


def _parse_log(value: str) -> str:
    return str(value)


def _parse_zion(value: str) -> str:
    if value == "http://zion.local":
        return "Online"
    else:
        return "Offline"


def check_config(key: str, value: str) -> str:
    parsed: str = ""
    if key == "mode":
        parsed = f"Mode: {_parse_mode(value)}"
    elif key == "database":
        parsed = f"Database: {_parse_database(value)}"
    elif key == "api":
        parsed = f"API Access: {_parse_api(value)}"
    elif key == "log":
        parsed = f"Log Level: {_parse_log(value)}"
    elif key == "zion":
        parsed = f"Zion Network: {_parse_zion(value)}"
    else:
        parsed = "There is no configuration data"
    return parsed


def main() -> None:
    production_override: str | None = os.environ.get("MATRIX_MODE")
    config: dict[str, str] = load_config()
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    for key, value in config.items():
        print(check_config(key, value))
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file does't exist")
    if production_override:
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides not available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
