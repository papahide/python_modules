import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using:'import alchemy' structure to access potions")
    strength: str = alchemy.strength_potion()
    print(f"Testing strength_potion: {strength}")
    heal: str = alchemy.heal()
    print(f"Testing heal alias: {heal}")


if __name__ == "__main__":
    main()
