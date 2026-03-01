
class GardenError(Exception):
    """
    Father Class that inherits fron Exception
    Used for Garden errors
    """
    pass


class PlantError(GardenError):
    """
    Child Class that inherits fron GardenError
    Used for Plant errors
    """
    pass


class WaterError(GardenError):
    """
    Child Class that inherits fron PlantError
    Used for Water errors
    """
    pass


def test_plant(days_without_water: int, plant: str) -> None:
    """
    Tester for plants error
    """
    if days_without_water >= 14:
        raise PlantError(f"The {plant} plant is wilting!")


def test_water(water_level: int) -> None:
    """
    Tester for water error
    """
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def main() -> None:
    """
    Main function that passes the arguments to all cases for testing
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError..")
    plant = "tomato"
    try:
        test_plant(20, plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        test_water(1)
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant(15, "Amorphophallus titanum")
    except GardenError as err:
        print(f"Caught PlantError: {err}")

    try:
        test_water(1)
    except GardenError as err:
        print(f"Caught WaterError: {err}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
