import sys
from typing import TextIO


def file_display(file_content: str, filename: str) -> None:
    print("---\n")
    print(f"{file_content}")
    print("\n---")
    print(f"File '{filename}' closed.\n")


def file_transform(file_content: str) -> str:
    print("Transform data:")
    new_content: str = ""
    for char in file_content:
        if char == "\n":
            new_content += "#\n"
        else:
            new_content += char
    return new_content


def save_new_data(new_content: str, new_name: str) -> None:
    new_file: TextIO = open(new_name, "w")
    new_file.write(new_content)
    new_file.close()


def file_actions(file_name: str) -> None:
    file: TextIO = open(file_name, "r")
    file_content: str = file.read()
    file.close()
    filename: str = file.name
    file_display(file_content, filename)
    new_content: str = file_transform(file_content)
    print("---\n")
    print(f"{new_content}")
    print("\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip("\n")
    if not new_name:
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{new_name}'")
        try:
            save_new_data(new_content, new_name)
            print(f"Data saved in file '{new_name}'.\n")
        except FileNotFoundError as ferr:
            sys.stderr.write(f"[STDERR] Error opening "
                             f"file '{new_name}': {ferr}\n")
            print("Data not saved.")
        except PermissionError as perr:
            sys.stderr.write(f"[STDERR] Error opening "
                             f"file '{new_name}': {perr}\n")
            print("Data not saved.")
        except IsADirectoryError as derr:
            sys.stderr.write(f"[STDERR] Error opening "
                             f"file '{new_name}': {derr}\n")
            print("Data not saved.")


def main() -> None:
    argn: int = len(sys.argv)
    if argn < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file_actions(sys.argv[1])
        except FileNotFoundError as ferr:
            sys.stderr.write(f"[STDERR] Error opening "
                             f"file '{sys.argv[1]}': {ferr}")
        except PermissionError as perr:
            sys.stderr.write(f"[STDERR] Error opening "
                             f"file '{sys.argv[1]}': {perr}")
        except IsADirectoryError as derr:
            sys.stderr.write(f"[STDERR] Error opening "
                             f"file '{sys.argv[1]}': {derr}")


if __name__ == "__main__":
    main()
