
class PlantError(Exception):
    pass

def check_plant_health(plant_name: str, water_level: int, 
                       sunlight_hours: int) -> None:

    if plant_name is None:
        raise(PlantError("Error: Plant name cannot be empty!"))

    try:
        int(water_level)
    except ValueError as err:
        print(f"Error: {err}")

    if water_level < 1:
        raise(PlantError(f"Water level {water_level} is too low (min 1)"))
    elif water_level > 10:
        raise(PlantError(f"Water level {water_level} is too high (max 10)"))

    try:
        int(sunlight_hours)
    except ValueError as err:
        print(f"Error: {err}")

    if sunlight_hours < 2:
        raise(PlantError(f"Sunlight hours {sunlight_hours} is too low (min 2)"))
    elif sunlight_hours > 12:
        raise(PlantError(f"Sunlight hours {sunlight_hours} is too high (max 12)"))
    
    
