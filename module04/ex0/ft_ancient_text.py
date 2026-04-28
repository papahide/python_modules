import sys
from typing import TextIO


def file_read(file_name: str) -> None:
    file: TextIO = open(file_name)
    print("---\n")
    file_content: str = file.read()
    print(f"{file_content}")
    file.close()
    print("\n---")
    print(f"File '{file.name}' closed.")


def main() -> None:
    argn: int = len(sys.argv)
    if argn < 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file_read(sys.argv[1])
        except FileNotFoundError as ferr:
            print(f"Error opening file '{sys.argv[1]}': {ferr}\n")
        except PermissionError as perr:
            print(f"Error opening file '{sys.argv[1]}': {perr}\n")
        except IsADirectoryError as derr:
            print(f"Error opening file '{sys.argv[1]}': {derr}\n")


if __name__ == "__main__":
    main()
