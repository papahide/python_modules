import sys


def ft_no_args() -> None:
    print("No scores provided -_-, lame...")
    print("Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")


def ft_parse_args(args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in args:
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError as err:
            print(f"Error: {err}")
    return scores


def ft_args(args: list[str]):
    scores: list[int] = ft_parse_args(args)

    if not scores:
        ft_no_args()
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    average: float = sum(scores) / len(scores)
    print(f"Average score: {average}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    rrnge: int = max(scores) - min(scores)
    print(f"Score range: {rrnge}\n")


def main() -> None:
    print("=== Player Score Analytics ===")
    argn: int = len(sys.argv)
    if argn == 1:
        ft_no_args()
    elif argn > 1:
        ft_args(sys.argv[1:])


if __name__ == "__main__":
    main()
