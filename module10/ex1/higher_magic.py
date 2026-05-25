from collections.abc import Callable


def invisibility(target: str, power: int) -> str:
    return f"{target} gets invisibility for {power} seconds"


def unshowering(target: str, power: int) -> str:
    return (f"{target} gets {power} days"
            "without showering")


def drinking(target: str, power: int) -> str:
    return (f"{target} gets drunk with "
            f"{power} beers")


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]) -> Callable[[str, int],
                                                                  tuple[str,
                                                                        str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str,
                                        int], str]) -> Callable[[str,
                                                                 int], str]:
    def cast(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable[[str,
                                          int], str]]) -> Callable[[str, int],
                                                                   list[str]]:
    def cast_all(target: str, power: int) -> list[str]:
        result: list[str] = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return cast_all


def lol_shower(target: str, power: int) -> bool:
    if target == "lol" and power >= 1:
        return True
    return False


def main() -> None:
    print("\nTesting spell combiner:")
    combined = spell_combiner(invisibility, drinking)
    comb_result = combined("Pedro", 12)
    for c_res in comb_result:
        print(c_res)

    print("\nTesting power amplifier:")
    amplified = power_amplifier(drinking, 10)
    amp_result = amplified("Denis", 50)
    print(amp_result)

    print("\nTesting conditional caster:")
    conditional = conditional_caster(lol_shower, unshowering)
    conditional_result = conditional("Rick", 1)
    print(conditional_result)

    spells = [invisibility,
              unshowering,
              drinking]
    print("\nTesting power amplifier:")
    sequence = spell_sequence(spells)
    result_sequence = sequence("Rocio", 5)
    for seq in result_sequence:
        print(seq)


if __name__ == "__main__":
    main()
