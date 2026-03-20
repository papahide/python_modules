import sys


def ft_no_args() -> None:
    print("No arguments provided!")


def ft_args(argv: list[str]) -> None:
    print(f"Arguments received: {len(argv)}")
    i = 1
    for arg in argv:
        print(f"Argument {i}: {arg}")
        i += 1


def main() -> None:
    print("=== Command Quest ===")
    argn = len(sys.argv)
    if argn == 1:
        ft_no_args()
    prog_name = sys.argv[0]
    print(f"Program name: {prog_name}")
    if argn > 1:
        ft_args(sys.argv[1:])
    print(f"Total arguments: {argn}")


if __name__ == "__main__":
    main()
