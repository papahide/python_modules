import math


def ft_create_positions(positions: list[int]) -> tuple[int, ...]:
    pos = tuple(positions)
    print(f"Position created: {pos}")
    return pos


def ft_distance(p1: tuple[int, ...], p2: tuple[int, ...] | None) -> None:
    if p2 is not None:
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {p1} and {p2}: {distance:.2f}\n")
    else:
        return


def ft_parse_pos(spos: str) -> tuple[int, ...] | None:
    print(f"Parsing coordinates: \"{spos}\"")
    lpos = spos.split(',')
    coord: list[int] = []
    for p in lpos:
        try:
            num = int(p)
            coord.append(num)
        except ValueError as err:
            print(f"Error parsing coordinates: {err}")
            print(f"Error details - Type: {type(err).__name__}"
                  f", Args: {err.args}\n")
            return None
    pos = tuple(coord)
    print(f"Parsed position: {pos}")
    return tuple(pos)


def ft_coordinates(pos: tuple[int, ...]) -> tuple[int, ...]:
    return (pos)


def main() -> None:
    print("=== Game Coordinate System ===")
    pos_ini: tuple[int, int, int] = (0, 0, 0)

    """
    Valid coordinates and no parsing
    """
    pos: tuple[int, ...] | None = ft_create_positions([1, 2, 3])
    ft_distance(pos_ini, pos)

    """
    Valid coordinates with parsing
    """
    spos = "3,2,1"
    pos: tuple[int, ...] | None = ft_parse_pos(spos)
    ft_distance(pos_ini, pos)

    """
    Invalid coordinates
    """
    ipos = "asdf,adf,asdf"
    ft_parse_pos(ipos)

    if pos is not None:
        x, y, z = ft_coordinates(pos)
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
