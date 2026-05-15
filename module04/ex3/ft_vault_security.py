
def secure_archive(unchecked_file: str, mode: str, content: str
                   ) -> tuple[bool, str]:
    result: tuple[bool, str] = (True, 'ok')
    try:
        with open(unchecked_file, mode) as file:
            if mode == "w":
                file.write(content)
                return (True, 'Content successfully written to file')
            elif mode == "r":
                return (True, file.read())
            else:
                return (False, "Only modes available: r (read) and w (write)")
    excep as err:
        result = (False, str(err))
        return (result)
    except PermissionError as err:
        result = (False, str(err))
        return (result)


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("nonexistent.txt", "r", ""))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("inaccessible.txt", "r", ""))

    file_read: tuple[bool, str] = secure_archive("regular.txt", "r", "")
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(file_read)

    if file_read[0] is not False:
        print("\nUsing 'secure_archive' to write "
              "previous content to a new file:")
        print(secure_archive("hola.txt", "w", file_read[1]))


if __name__ == "__main__":
    main()
