from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Ranks(Enum):
    cadet = "Cadet"
    officer = "Officer"
    lieutenant = "Lieutenant"
    captain = "Captain"
    commander = "Commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Ranks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        has_leader = any(m.rank in [Ranks.captain, Ranks.commander]
                         for m in self.crew)
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")
        experienced = sum(1 for m in self.crew if m.years_experience >= 5)
        if self.duration_days > 365 and experienced < len(self.crew) / 2:
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")
        active_check = True
        for member in self.crew:
            if not member.is_active:
                active_check = False
        if not active_check:
            raise ValueError("All crew members must be active")
        return self


def display_mission(mission: SpaceMission) -> None:
    if not mission:
        return
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: {mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        sarah = CrewMember(
                        member_id="CM001",
                        name="Sarah Connor",
                        rank=Ranks.commander,
                        age=45,
                        specialization="Mission Command",
                        years_experience=15,
                        is_active=True)
        john = CrewMember(
                        member_id="CM002",
                        name="John Smith",
                        rank=Ranks.lieutenant,
                        age=38,
                        specialization="Navigation",
                        years_experience=8,
                        is_active=True)
        alice = CrewMember(
                        member_id="CM003",
                        name="Alice Johnson",
                        rank=Ranks.officer,
                        age=32,
                        specialization="Engineering",
                        years_experience=6,
                        is_active=True)

        vlalid_mission = SpaceMission(
                                mission_id="M2024_MARS",
                                mission_name="Mars Colony Establishment",
                                destination="Mars",
                                launch_date=datetime(2024, 7, 15),
                                duration_days=900,
                                budget_millions=2500.0,
                                crew=[sarah, john, alice])
        display_mission(vlalid_mission)
    except ValidationError as err:
        for error in err.errors():
            print(error["ctx"]["error"])
    print("\n=========================================")
    print("Expected validation error:")
    try:
        sarah = CrewMember(
                        member_id="CM001",
                        name="Sarah Connor",
                        rank=Ranks.commander,
                        age=45,
                        specialization="Mission Command",
                        years_experience=2,
                        is_active=True)
        john = CrewMember(
                        member_id="CM002",
                        name="John Smith",
                        rank=Ranks.lieutenant,
                        age=38,
                        specialization="Navigation",
                        years_experience=2,
                        is_active=True)
        alice = CrewMember(
                        member_id="CM003",
                        name="Alice Johnson",
                        rank=Ranks.officer,
                        age=32,
                        specialization="Engineering",
                        years_experience=2,
                        is_active=True)

        error_mission = SpaceMission(
                                mission_id="M2024_MARS",
                                mission_name="Mars Colony Establishment",
                                destination="Mars",
                                launch_date=datetime(2024, 7, 15),
                                duration_days=900,
                                budget_millions=2500.0,
                                crew=[sarah, john, alice])
        display_mission(error_mission)
    except ValidationError as err:
        for error in err.errors():
            print(error["ctx"]["error"])


if __name__ == "__main__":
    main()
