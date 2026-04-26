import random


class Player:
    def __init__(self, name: str, achievements: set[str]) -> None:
        self.name = name
        self.achievements = achievements


def gen_player_achievements() -> set[str]:
    total_ach: list[str] = ['Crafting Genius', 'World Savior',
                            'Master Explorer', 'Collector Supreme',
                            'Untouchable', 'Boss Slayer',
                            'Strategist', 'Speed Runner',
                            'Survivor', 'Treasure Hunter',
                            'First Steps', 'Sharp Mind',
                            'Unstopable']
    ach_len = random.randint(4, 10)
    ach_player = random.sample(total_ach, k=ach_len)
    return set(ach_player)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players: dict[str, set[str]] = {"Alice": gen_player_achievements(),
                                    "Bob": gen_player_achievements(),
                                    "Charlie": gen_player_achievements(),
                                    "Dylan": gen_player_achievements()}

    for name, acheivements in players.items():
        print(f"Player {name}: {acheivements}")

    all_distinct: set[str] = set()

    all_values = list(players.values())
    common: set[str] = all_values[0].intersection(*all_values[1:])

    for ach in players.values():
        all_distinct = all_distinct.union(ach)

    print(f"\nAll distinct achievements: {all_distinct}\n")
    print(f"\nCommon achievements: {common}\n")

    for name, acheivements in players.items():
        others: list[set[str]] = []
        for n, s in players.items():
            if n != name:
                others.append(s)
        print(f"Only {name} has: {acheivements.difference(*others)}")

    print("\n")

    for name, acheivements in players.items():
        print(f"{name} is missing: {all_distinct.difference(acheivements)}")


if __name__ == "__main__":
    main()
