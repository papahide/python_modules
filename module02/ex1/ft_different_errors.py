
def garden_operations(error: str) -> None:
    match error:
        case "ValueError":
            int("hol")
        case "ZeroDivisionError":
            10 / 0
        case "FileNotFoundError":
            open("missing.txt", "r")
        case "KeyError":
            plant = {"fruta": "platano"}
            plant["hola"]

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    errors: list[str] = ["ValueError", "ZeroDivisionError",
                         "FileNotFoundError", "KeyError"]

    for error in errors:
        print(f"\nTesting {error}...")
        try:
            garden_operations(error)
        except ValueError:
            print(f"Caught {error}: invalid literal for int()")
        except ZeroDivisionError as err:
            print(f"Caught {error}: {err}")
        except FileNotFoundError as err:
            print(f"Caught {error}: {err}")
        except KeyError as err:
            print(f"Caught {error}: {err}")
    print(f"\nTesting multiple errors together...")

    try:
        garden_operations(error)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print(f"Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
