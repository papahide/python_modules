import math


def get_player_pos() -> tuple[float, float, float]:
    """
    permitted = "0123456789.-, "
    """
    while True:
        coord_str = input("Enter new coordinates as floats in format 'x,y,z': ")

        comma_count = 0
        for char in coord_str:
            if char == ",":
                comma_count += 1

        if comma_count != 2:
            print("Invalid syntax")
            continue

        final_coords: list[float] = []
        current_nbr = ""
        error = False

        try:
            for char in coord_str + ",":
                if char == ",":
                    try:
                        if current_nbr:
                            final_coords.append(float(current_nbr))
                            current_nbr = ""
                        else:
                            raise ValueError
                    except ValueError:
                        print(f"Error on parameter '{current_nbr}': could not convert string to float: '{current_nbr}'")
                        error = True
                        break
                elif char != " ":
                    current_nbr += char

            if error:
                continue

            if len(final_coords) == 3:
                return (final_coords[0], final_coords[1], final_coords[2])
            else:
                print("Invalid syntax")

        except Exception:
            print("Invalid syntax")


def ft_display_coords(coords: tuple[float, float, float]) -> None:
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


def ft_distance(p1: tuple[float, float, float], p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def main() -> None:
    print("=== Game Coordinate System ===\n")
    pos_ini: tuple[int, int, int] = (0, 0, 0)
    print("Get a first set of coordinates")
    first_coord: tuple[float, ...] = get_player_pos()
    ft_display_coords(first_coord)
    dist_center: float = ft_distance(pos_ini, first_coord)
    print(f"Distance to center: {dist_center:.4f}")

    print("\nGet a second set of coordinates")
    second_coord = get_player_pos()
    dist_points: float = ft_distance(first_coord, second_coord)
    print(f"Distance to center: {dist_points:.4f}")


if __name__ == "__main__":
    main()
