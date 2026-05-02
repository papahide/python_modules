import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using:'import ...' structure to access elements.py")
    fire: str = elements.create_fire()
    print(f"Testing create_fire: {fire}\n")


if __name__ == "__main__":
    main()
