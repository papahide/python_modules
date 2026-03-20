class Player:
    def __init__(self, name: str, achievements: set[str]) -> None:
        self.name = name
        self.achievements = achievements


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = Player("Alice", {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'})
    bob = Player("Bob",  {'first_kill', 'level_10', 'boss_slayer', 'collector'})
    charlie = Player("Charlie", {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'})
    players = [alice, bob, charlie]

    for player in players:
        print(f"Player {player.name} achievements: {player.achievements}")

    a_ach = alice.achievements
    b_ach = bob.achievements
    c_ach = charlie.achievements
    print("\n=== Achievement Analytics ===")
    unique_ach = a_ach.union(b_ach, c_ach)
    print(f"All unique achievements: {unique_ach}")
    print(f"Total unique achievements: {len(unique_ach)}\n")

    a = a_ach - b_ach - c_ach
    b = b_ach - a_ach - c_ach
    c = c_ach - a_ach - b_ach
    print(f"Common to all players: {a_ach.intersection(b_ach, c_ach)}")
    print(f"Rare achievements (1 player): {a.union(b, c)}\n")

    print(f"Alice vs Bob common: {a_ach.intersection(b_ach)}")
    print(f"Alice unique: {a_ach.difference(b_ach)}")
    print(f"Bob unique: {b_ach.difference(a_ach)}")


if __name__ == "__main__":
    main()
