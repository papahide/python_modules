from functools import reduce, partial
from typing import Any
from collections.abc import Callable
from operator import add, mul
from functools import lru_cache
from functools import singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        print("No valid operaation provided")
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    versions: dict[str, Callable] = {"sword": partial(base_enchantment,
                                                      power=50,
                                                      element="fire"),
                                     "ice cream": partial(base_enchantment,
                                                          power=50,
                                                          element="ice"),
                                     "stairs": partial(base_enchantment,
                                                       power=50,
                                                       element="rock solid")}
    return versions


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


@singledispatch
def cast(spell):
    return "Unknown spell type"


@cast.register(int)
def _(spell):
    return f"Damage spell: {spell} damage"


@cast.register(str)
def _(spell):
    return f"Enchantment: {spell}"


@cast.register(list)
def _(spell):
    return f"Multi-cast: {len(spell)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    return cast


def main() -> None:
    print("\nTesting spell reducer...")
    print(f"Sum: {str(spell_reducer([1, 2, 3], 'add'))}")
    print(f"Product: {str(spell_reducer([1, 2, 3], 'multiply'))}")
    print(f"Max: {str(spell_reducer([1, 2, 3], 'max'))}")
    print(f"Min: {str(spell_reducer([1, 0, 3], 'min'))}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(f"{spell(42)}")
    print(f"{spell('fireball')}")
    print(f"{spell([1, 2, 3])}")
    print(f"{spell(2.3)}")


if __name__ == "__main__":
    main()
