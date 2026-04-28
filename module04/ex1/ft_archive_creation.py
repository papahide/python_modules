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
    new_name: str = input("Enter new file name (or empty): ")
    if not new_name:
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{new_name}'")
        save_new_data(new_content, new_name)
        print(f"Data saved in file '{new_name}'.\n")


def main() -> None:
    argn: int = len(sys.argv)
    if argn < 2:
        print("Usage: ft_archive_creation.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file_actions(sys.argv[1])
        except FileNotFoundError as ferr:
            print(f"Error opening file '{sys.argv[1]}': {ferr}\n")
        except PermissionError as perr:
            print(f"Error opening file '{sys.argv[1]}': {perr}\n")
        except IsADirectoryError as derr:
            print(f"Error opening file '{sys.argv[1]}': {derr}\n")


if __name__ == "__main__":
    main()
