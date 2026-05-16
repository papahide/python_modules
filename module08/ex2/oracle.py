from dotenv import load_dotenv
import os


def load_config() -> dict[str, str]:
    load_dotenv()
    config: dict[str, str] = {"mode": os.getenv("MATRIX_MODE", "development"),
                              "database": os.getenv("DATABASE_URL",
                                                    "http://localhost/phpmyadmin"),
                              "api": os.getenv("API_KEY", "NO CONFIGURATION"),
                              "log": os.getenv("LOG_LEVEL", "DEBUG"),
                              "zion": os.getenv("ZION_ENDPOINT", "http://zion.local")
                              }
    return config


def check_config() -> str:
    if 


def main() -> None:
    config: dict[str, str] = load_config()
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    for key, value in config.items():
        print(f"{key.capitalize()}: {check_config(key, value)}")



if __name__ == "__main__":
    main()