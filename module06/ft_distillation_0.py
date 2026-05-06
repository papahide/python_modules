from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    strength_p: str = potions.strength_potion()
    print(f"Testing strength_potion: {strength_p}")
    healing_p: str = potions.healing_potion()
    print(f"Testing healing_potion: {healing_p}\n")


if __name__ == "__main__":
    main()
