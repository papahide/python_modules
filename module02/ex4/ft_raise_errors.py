
class PlantError(Exception):
    pass


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:

    try:
        int(water_level)
    except ValueError as err:
        print(f"Error: {err}")

    try:
        int(sunlight_hours)
    except ValueError as err:
        print(f"Error: {err}")

    if not plant_name:
        raise (PlantError("Plant name cannot be empty!"))

    if water_level < 1:
        raise (PlantError(f"Water level {water_level} "
                          f"is too low (min 1)"))
    elif water_level > 10:
        raise (PlantError(f"Water level {water_level} "
                          f"is too high (max 10)"))

    if sunlight_hours < 2:
        raise (PlantError(f"Sunlight hours {sunlight_hours} "
                          f"is too low (min 2)"))
    elif sunlight_hours > 12:
        raise (PlantError(f"Sunlight hours {sunlight_hours} "
                          f"is too high (max 12)"))

    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:

    print("=== Garden Plant Health Checker ===")

    test_cases: list[dict] = [
        {
            "test_name": "Testing good values...",
            "name": "Welwitschia mirabilis",
            "water": 2,
            "sun": 12
        },
        {
            "test_name": "Testing empty plant name...",
            "name": "",
            "water": 8,
            "sun": 4
        },
        {
            "test_name": "Testing bad water level...",
            "name": "Rafflesia arnoldii",
            "water": 0,
            "sun": 10
        },
        {
            "test_name": "Testing bad sunlight hours...",
            "name": "Amorphophallus titanum",
            "water": 7,
            "sun": 50
        }
    ]

    for test in test_cases:
        print(f"\n{test["test_name"]}")
        try:
            message = check_plant_health(test["name"],
                                         test["water"],
                                         test["sun"])
            if message:
                print(message)
        except PlantError as err:
            print(f"Error: {err}")

    print("\nAll error raising tests completed!")


def main():
    test_plant_checks()


if __name__ == "__main__":
    main()
