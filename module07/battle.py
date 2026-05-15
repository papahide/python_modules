import ex0


def check_factory(factory: ex0.CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def creature_fight(creature_1: ex0.CreatureFactory,
                   creature_2: ex0.CreatureFactory) -> None:
    c1_base = creature_1.create_base()
    c2_base = creature_2.create_base()
    print(c1_base.describe())
    print(" vs.")
    print(c2_base.describe())
    print(" fight!")
    print(c1_base.attack())
    print(c2_base.attack())


def main() -> None:
    print("Testing factory")
    flame_fact = ex0.FlameFactory()
    check_factory(flame_fact)
    print("\nTesting factory")
    aqua_fact = ex0.AquaFactory()
    check_factory(aqua_fact)
    print("\nTesting battle")
    creature_fight(flame_fact, aqua_fact)


if __name__ == "__main__":
    main()
