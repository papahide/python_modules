

def ft_display_hscore(players: list[dict[str, int | str]]) -> None:
    hi_scorers: list[str] = []

    for player in players:
        score_value = player.get('score', 0)

        if isinstance(score_value, int) and score_value > 2000:
            name = player.get('name', 'Unknown')

            if isinstance(name, str):
                hi_scorers.append(str(name))

    print(f"High scorers (>2000): {hi_scorers}")

def ft_display_dscore(players: list[dict[str, int | str]]) -> None:
    double: list[int] = []
    seen: list[int] = []
    for player in players:
        score = player.get('score', 0)
        if isinstance(score, int):
            if score in seen:
                if score not in double:
                    double.append(score)
            else:
                seen.append(score)
    print(f"Scores doubled: {double}")


def ft_display_active(players: list[dict[str, str | int | bool]]):
    active_players: list[str] = []
    for player in players:
        is_active = player.get('active', False)
        name = player.get('name', 'Unknown')
        if is_active is True and isinstance(name, str):
            if is_active == True:
                active_players.append(name)
    print(f"Active players: {active_players}")



def main() -> None:
    players: list[dict[str, str | int | bool]] = [
                                           {'name': 'alice', 'score': 1800, 'active': True},
                                           {'name': 'bob', 'score': 1800, 'active': True},
                                           {'name': 'charlie', 'score': 2150, 'active': False},
                                           {'name': 'diana', 'score': 300, 'active': False},
                                           {'name': 'pepe', 'score': 500, 'active': True},
                                           {'name': 'aquiles', 'score': 300, 'active': True},
                                           {'name': 'dolores', 'score': 2150, 'active': False}
                                           ]
    achievements = [
                    "first_kill",
                    "first_kill",
                    "level_10",
                    "tutorial_death",
                    "wrong_jump",
                    "npc_talk",
                    "wall_climb",
                    "phone_fall",
                    "self_boom",
                    "bad_save"
                    ]
    
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    ft_display_hscore(players)
    ft_display_dscore(players)
    ft_display_active(players)

    print("\n=== Dict Comprehension Examples ===")
    

if __name__ == "__main__":
    main()