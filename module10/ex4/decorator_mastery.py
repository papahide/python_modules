from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting function {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"Spell completed in {finish - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power") or (args[2] if len(args) > 2 else 0)
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace()
            for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell():
    raise Exception("Spell unstable!")


def main() -> None:
    print("\nTesting spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    retry = unstable_spell()
    print(retry)

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Gandalf"))
    print(mage.validate_mage_name("007"))
    print(mage.cast_spell("Fatal strike", 12))
    print(mage.cast_spell("Fatal strike", 3))


if __name__ == "__main__":
    main()
