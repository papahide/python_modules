
class PlantError(Exception):
    """
    Custom error class for plants
    """
    pass

def test_watering_plants(plant: str) -> None:
    """
    Waters the plant and
    Raises a custom PlatError if plant is None
    """
    if plant is None:
        raise PlantError("Cannot water None - invalid plant!")
    else:
        print(f"Watering {plant}")

def water_plants(plant_list: list) -> None:
    """
    Iterates every plant to water
    If there is a plant error it displays it
    Executes finally
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            test_watering_plants(plant)
        print("Watering completed successfully!")
    except PlantError as err:
        print(f"Error: {err}")
    finally:
        print("Closing watering system (cleanup)")

def main():
    """
    Main function to test the watering system with and without errors
    """
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")

    plants: list = [
        "Welwitschia mirabilis",
        "Rafflesia arnoldii",
        "Dionaea muscipula",
        "Amorphophallus titanum"]
    water_plants(plants)

    print("\nTesting with error...")

    plants_error: list = [
        "Welwitschia mirabilis",
        "Rafflesia arnoldii",
        None,
        "Amorphophallus titanum"]
    water_plants(plants_error)

    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    main()