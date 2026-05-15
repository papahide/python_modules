from abc import ABC, abstractmethod
from ex0.creatures import Creature
from typing import cast
from ex1.capabilities import TransformCapability, HealCapability


class ActionError(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self, strategy_name: str) -> None:
        self.name: str = strategy_name

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("normal")

    def is_valid(self, creature: Creature) -> bool:
        if creature:
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise ActionError(f"Invalid Creature '{creature.name}' "
                              f"for this {self.name} strategy")


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("aggressive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            tr_creature = cast(TransformCapability, creature)
            creature_attack = cast(Creature, tr_creature)
            print(tr_creature.transform())
            print(creature_attack.attack())
            print(tr_creature.revert())
        else:
            raise ActionError(f"Invalid Creature '{creature.name}' "
                              f"for this {self.name} strategy")


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("defensive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            heal_creature = cast(HealCapability, creature)
            creature_attack = cast(Creature, heal_creature)
            print(creature_attack.attack())
            print(heal_creature.heal())
        else:
            raise ActionError(f"Invalid Creature '{creature.name}' "
                              f"for this {self.name} strategy")
