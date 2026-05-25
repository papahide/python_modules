from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def increase_counter() -> int:
        nonlocal count
        count += 1
        return count
    return increase_counter


def spell_accumulator(initial_power: int) -> Callable:
    def acumulate_power(acumulate: int) -> int:
        nonlocal initial_power
        initial_power += acumulate
        return initial_power
    return acumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_item(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant_item


def memory_vault() -> dict[str, Callable]:
    storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key) -> Any:
        return storage.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    mage = mage_counter()
    for i in range(3):
        print(f"Call {i}: {mage()}")

    print("\nTesting spell accumulator...")
    base: int = 1000
    spell_accumulate = spell_accumulator(base)
    print(f"Base {base}, add 345: {spell_accumulate(345)}")
    print(f"Base {base}, add -540: {spell_accumulate(-540)}")
    print(f"Base {base}, add 96: {spell_accumulate(96)}")

    print("\nTesting enchantment factory...")
    spell_1 = enchantment_factory("Animate")
    print(spell_1("Sausage"))
    spell_2 = enchantment_factory("Lubricate")
    print(spell_2("Staircase"))
    spell_3 = enchantment_factory("Illuminate")
    print(spell_3("Cheese"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print(f"Store \'secret\' = {vault["store"]("secret", 42)}")
    print(f"Recall \'secret\' = {vault["recall"]("secret")}")
    print(f"Recall \'unknown\' = {vault["recall"]("unknown")}")


if __name__ == "__main__":
    main()
