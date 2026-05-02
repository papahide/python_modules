import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    air: str = alchemy.create_air()
    print(f"Testing create_air: {air}\n")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    earth: str = alchemy.create_earth()  # type: ignore
    print(f"Testing the hidden create_earth: {earth}\n")


if __name__ == "__main__":
    main()
