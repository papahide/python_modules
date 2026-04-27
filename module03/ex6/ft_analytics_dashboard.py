import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players: list[str] = ['Alice', 'bob',
                          'Charlie', 'dylan',
                          'Emma', 'Gregory',
                          'john', 'kevin',
                          'Liam']
    to_cap_play: list[str] = [player.capitalize() for player in players]
    capitalize_play: list[str] | None = [
        player for player in players if player[0].isupper()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {to_cap_play}")
    print(f"New list of capitalized names only: {capitalize_play}")

    players_scores: dict[str, int] = {}
    players_scores = {
        play: random.randint(0, 1000)
        for play in capitalize_play}

    print(f"Score dict: {players_scores}")

    avg: float = sum(players_scores.values()) / len(players_scores)

    print(f"Score average is {avg:.2f}")

    h_scores: dict[str, int] = {
        play: players_scores[play]
        for play in players_scores
        if players_scores[play] > avg}

    print(f"High scores: {h_scores}")


if __name__ == "__main__":
    main()
