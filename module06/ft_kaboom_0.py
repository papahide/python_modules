def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    from alchemy.grimoire import light_spell_record
    spell: str = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {spell}\n")


if __name__ == "__main__":
    main()
