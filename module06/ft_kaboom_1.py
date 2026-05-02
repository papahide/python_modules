def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    spell: str = dark_spell_record("Fantasy", "Bats and frogs")
    print(f"Testing record light spell: {spell}")


if __name__ == "__main__":
    main()
