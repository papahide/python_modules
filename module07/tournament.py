import ex0
import ex1
import ex2


def battle(opponent1: tuple[ex0.CreatureFactory,
                            ex2.BattleStrategy],
           opponent2: tuple[ex0.CreatureFactory,
                            ex2.BattleStrategy]) -> None:
    print("\n* Battle *")
    creature1 = opponent1[0].create_base()
    creature2 = opponent2[0].create_base()
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" now fight!")
    try:
        opponent1[1].act(creature1)
        opponent2[1].act(creature2)
    except ex2.ActionError as err:
        print(f"Battle error, aborting tournament: {err}")


def single_battle(opponents: list[tuple[ex0.CreatureFactory,
                                  ex2.BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            battle(opponents[i], opponents[j])


def tournament_format(tourn: list[tuple[ex0.CreatureFactory,
                                        ex2.BattleStrategy]]) -> str:
    parts: list[str] = []
    for factory, strategy in tourn:
        if isinstance(factory, (ex1.TransformCreatureFactory,
                                ex1.HealingCreatureFactory)):
            parts.append(f"({factory.create_base().family_name}+"
                         f"{strategy.name.capitalize()})")
        else:
            parts.append(f"({factory.create_base().name}+"
                         f"{strategy.name.capitalize()})")
    return "[ " + ", ".join(parts) + " ]"


def tournament_output(tournament: list[tuple[ex0.CreatureFactory,
                                             ex2.BattleStrategy]], ) -> None:
    print(" " + tournament_format(tournament))
    print("*** Tournament ***")
    print(f"{len(tournament)} opponents involved")
    single_battle(tournament)


def main() -> None:
    """
    Strategies:
    """
    n_strategy = ex2.NormalStrategy()
    a_strategy = ex2.AggressiveStrategy()
    d_strategy = ex2.DefensiveStrategy()
    """
    Factories:
    """
    f_fact = ex0.FlameFactory()
    a_fact = ex0.AquaFactory()
    h_fact = ex1.HealingCreatureFactory()
    t_fact = ex1.TransformCreatureFactory()
    """
    Tournaments:
    """
    tourn_0: list[tuple[ex0.CreatureFactory,
                        ex2.BattleStrategy]] = [(f_fact, n_strategy),
                                                (h_fact, d_strategy)]
    tourn_1: list[tuple[ex0.CreatureFactory,
                        ex2.BattleStrategy]] = [(f_fact, a_strategy),
                                                (h_fact, d_strategy)]
    tourn_2: list[tuple[ex0.CreatureFactory,
                        ex2.BattleStrategy]] = [(a_fact, n_strategy),
                                                (h_fact, d_strategy),
                                                (t_fact, a_strategy)]
    tournaments: dict[str, list[tuple[ex0.CreatureFactory,
                                      ex2.BattleStrategy]]] = {}
    tournaments["(basic)"] = tourn_0
    tournaments["(error)"] = tourn_1
    tournaments["(multiple)"] = tourn_2
    """
    Outputs:
    """
    for i, (tour_type, value) in enumerate(tournaments.items()):
        print(f"\nTournament {i} {tour_type}")
        tournament_output(value)


if __name__ == "__main__":
    main()
