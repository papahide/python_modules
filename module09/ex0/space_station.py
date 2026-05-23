from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10, alias="ID")
    name: str = Field(min_length=1, max_length=50, alias="Name")
    crew_size: int = Field(ge=1, le=20, alias="Crew")
    power_level: float = Field(ge=0.0, le=100.0, alias="Power")
    oxygen_level: float = Field(ge=0.0, le=100.0, alias="Oxygen")
    is_operational: bool = True
    notes: Optional[str] = Field(min_length=0, max_length=100, alias="Notes")
    last_maintenance: datetime = datetime(2000, 1, 1)


def display_station(station: SpaceStation) -> None:
    for key, value in station.model_dump(by_alias=True).items():
        if key == "last_maintenance":
            continue
        if key == "is_operational" and value:
            print("Status: Operational")
            continue
        if value:
            suffix = "%" if key in ("Power", "Oxygen") else ""
            people = " people" if key == "Crew" else ""
            print(f"{key}: {value}{suffix}{people}")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        print("Valid station created:")
        station = SpaceStation(ID="ISS001",
                               Name="International Space Station",
                               Crew=6,
                               Power=85.5,
                               Oxygen=92.3,
                               is_operational=True,
                               Notes="Don't open trap door..")
        display_station(station)
    except ValidationError as err:
        for error in err.errors():
            print(error["msg"])
    print("\n========================================")
    try:
        station = SpaceStation(ID="ISS001",
                               Name="International Space Station",
                               Crew=25,
                               Power=200.5,
                               Oxygen=92.3,
                               is_operational=True,
                               Notes="Don't open trap door..")
        display_station(station)
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
