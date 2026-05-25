def artifact_sorter(artifacts: list[dict[str,
                                         str | int]]) -> list[dict[str,
                                                                   str | int]]:
    return sorted(artifacts, key=lambda x: int(x['power']), reverse=True)


def power_filter(mages: list[dict[str, str | int]],
                 min_power: int) -> list[dict[str, str | int]]:
    return list(filter(lambda x: int(x['power']) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str,
                                str | int]]) -> dict[str,
                                                     str | int | float]:
    most_powerful = max(mages, key=lambda x: x['power'])
    least_powerful = min(mages, key=lambda x: x['power'])
    powers = list(map(lambda x: int(x['power']), mages))
    average_power: float = float(sum(powers) / len(powers))
    stats: dict[str, str | int | float] = {}
    stats['max_power'] = most_powerful['power']
    stats['min_power'] = least_powerful['power']
    stats['avg_power'] = average_power
    return stats


def main() -> None:
    artifacts: list[dict[str, str | int]] = [
                                             {"name": "Garbanzo",
                                              "power": 1,
                                              "type": "herb"},
                                             {"name": "LOL",
                                              "power": -30,
                                              "element": "smelly"},
                                             {"name": "calculator",
                                              "power": 10000,
                                              "element": "cerebral"},
                                             {"name": "Jack Daniels",
                                              "power": 10000000,
                                              "element": "power up"}]

    mages: list[dict[str, str | int]] = [
                                         {"name": "Irene",
                                          "power": 5,
                                          "element": "vegetarian"},
                                         {"name": "Denis2",
                                          "power": 7,
                                          "element": "hikikomori"},
                                         {"name": "Pedro",
                                          "power": 9,
                                          "element": "chineese"},
                                         {"name": "Denis1",
                                          "power": 8,
                                          "element": "rumano"}]

    spells: list[str] = ["invisibility", "unbathe", "do math", "drink"]

    print("\nTesting artifact sorter:")
    sorted_art = artifact_sorter(artifacts)
    for artifact in sorted_art:
        print(f"{artifact["name"]} -> {artifact["power"]}")

    print("\nTesting power filter:")
    filtered_mages = power_filter(mages, min_power=5)
    for mage in filtered_mages:
        print(f"{mage["name"]} -> {mage["power"]}")

    print("\nTesting spell transformer:")
    trans_spelled = spell_transformer(spells)
    for spell in trans_spelled:
        print(spell)

    print("\nTesting mage stats:")
    stats = mage_stats(mages)
    for key, value in stats.items():
        print(f"{key} -> {value}")


if __name__ == "__main__":
    main()
