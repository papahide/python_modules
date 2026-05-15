import ex1


def h_base_test(factory: ex1.HealingCreatureFactory) -> None:
    h_base = factory.create_base()
    print(h_base.describe())
    print(h_base.attack())
    print(h_base.heal())


def h_evolved_test(factory: ex1.HealingCreatureFactory) -> None:
    h_evolved = factory.create_evolved()
    print(h_evolved.describe())
    print(h_evolved.attack())
    print(h_evolved.heal())


def t_base_test(factory: ex1.TransformCreatureFactory) -> None:
    t_base = factory.create_base()
    print(t_base.describe())
    print(t_base.attack())
    print(t_base.transform())
    print(t_base.attack())
    print(t_base.revert())


def t_evolved_test(factory: ex1.TransformCreatureFactory) -> None:
    h_evolved = factory.create_evolved()
    print(h_evolved.describe())
    print(h_evolved.attack())
    print(h_evolved.transform())
    print(h_evolved.attack())
    print(h_evolved.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    h_b_factory = ex1.HealingCreatureFactory()
    h_base_test(h_b_factory)
    print(" evolved:")
    h_e_factory = ex1.HealingCreatureFactory()
    h_evolved_test(h_e_factory)
    print("\n Testing Creature with transform capability")
    print(" base:")
    t_b_factory = ex1.TransformCreatureFactory()
    t_base_test(t_b_factory)
    print(" evolved:")
    t_e_factory = ex1.TransformCreatureFactory()
    t_evolved_test(t_e_factory)


if __name__ == "__main__":
    main()
