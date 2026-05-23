from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = datetime(2000, 10, 3)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Alien Contact must start with \"AC\"")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and \
           self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should "
                             "include received messages")
        return self


def display_alien_contact(alien_contact: AlienContact) -> None:
    if not alien_contact:
        return
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type.value}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}/10")
    print(f"Duration: {alien_contact.duration_minutes} minutes")
    print(f"Witnesses: {alien_contact.witness_count} witnesses")
    if alien_contact.message_received:
        print(f"Message: '{alien_contact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        print("Valid contact report:")
        valid_alien_contact = AlienContact(contact_id="AC_2024_001",
                                           contact_type=ContactType.telepathic,
                                           location="Area 51, Nevada",
                                           signal_strength=8.5,
                                           duration_minutes=45,
                                           witness_count=5,
                                           message_received="Greetings "
                                           "from Zeta Reticuli")
        display_alien_contact(valid_alien_contact)
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            print(error["msg"])
    print("\n======================================")
    try:
        error_alien_contact = AlienContact(contact_id="_2024_001",
                                           contact_type=ContactType.telepathic,
                                           location="dasdfds",
                                           signal_strength=0,
                                           duration_minutes=45,
                                           witness_count=2,
                                           message_received="Greetings from"
                                           "Zeta Reticuli")
        display_alien_contact(error_alien_contact)
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
