from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    def __init__(self) -> None:
        self.family_name: str = "Healing"

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.family_name: str = "Transform"
        self.transf: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transf:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transf = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transf = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transf:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transf = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transf = False
        return f"{self.name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
