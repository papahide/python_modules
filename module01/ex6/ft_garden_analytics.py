
class Plant:
    """
    Father Plant Class
    """
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    """
    Child class that inherits from
    Plant and father class of PrizeFlower
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.flower_color = color
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    """
    Child class that inherits from
    FloweringPlant
    """
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize


class GardenManager:
    """
    Class methods operate on the class itself
    rather than on individual instances
    """
    total_gardens: int = 0
    managers: dict[str, "GardenManager"] = {}

    @classmethod
    def create_garden_network(cls) -> None:

        print(f"Total gardens managed: {cls.total_gardens}")

    @classmethod
    def get_points(cls) -> None:
        """
        Calculates global garden statistics.
        It doesn't belong to a single manager.
        It belongs to the whole system.
        """
        score = "Garden scores -"
        for name, manager in cls.managers.items():
            points = cls.GardenStats.calculate_score(manager.plants)
            score += f" {name}: {points}"
        print(score)

    class GardenStats:
        """
        Do not use self
        Do not use cls
        Just process data passed as arguments
        """
        @staticmethod
        def total_growth(plants: list, growth=1) -> int:
            """
            Calculates the total growth
            """
            total = 0
            for plant in plants:
                total += growth
            return total

        @staticmethod
        def total_plants(plants: list) -> int:
            """
            Calculates the plants added
            """
            total = 0
            for plant in plants:
                total += 1
            return total

        @staticmethod
        def count_type(plants: list) -> dict:
            """
            Counts how many of every type  of Plant
            """
            counts = {'regular': 0, 'flowering': 0, 'prize flowers': 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts['prize flowers'] += 1
                elif isinstance(plant, FloweringPlant):
                    counts['flowering'] += 1
                else:
                    counts['regular'] += 1
            return counts

        @staticmethod
        def height_validate(height: int) -> int:
            return height > 0

        @staticmethod
        def calculate_score(plants: list) -> int:
            """
            Calculates the score
            """
            points = 0
            for plant in plants:
                points += plant.height
                if isinstance(plant, PrizeFlower):
                    points += plant.prize_points
            return points

    def __init__(self, name: str) -> None:
        self.owner_name = name
        self.plants = []
        GardenManager.total_gardens += 1
        GardenManager.managers[self.owner_name] = self

    def add_plants(self, plants: list) -> None:
        """
        Adds all the plants to the garden manager passed through a list
        """
        for plant in plants:
            if GardenManager.GardenStats.\
               height_validate(plant.height) is False:
                return
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_plants(self, growth=1) -> None:
        """
        Makes the plants grow (increase height)
        """
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.height += growth
            print(f"{plant.name} grew {growth}cm")

    def garden_report(self) -> None:
        """
        Prints the report of the garden of a manager
        """
        print("Plants in garden:")
        for plant in self.plants:
            output = f"- {plant.name}: {plant.height}cm"
            if isinstance(plant, FloweringPlant):
                output += f", {plant.flower_color} flowers (blooming)"
            if isinstance(plant, PrizeFlower):
                output += f", Prize points: {plant.prize_points}"
            print(output)
        print(f"\nPlants added: "
              f"{GardenManager.GardenStats.total_plants(self.plants)}, "
              f"Total growth = "
              f"{GardenManager.GardenStats.total_growth(self.plants)}cm")
        flower_type = GardenManager.GardenStats.count_type(self.plants)
        print(f"Plant types: {flower_type['regular']} regular, "
              f"{flower_type['flowering']} flowering, "
              f"{flower_type['prize flowers'] } prize flowers")


def main() -> None:
    """
    Main function witch checkes that everything runs correctly
    """
    print("=== Garden Management System Demo ===\n")
    plants1 = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]
    manager1 = GardenManager("Alice")
    # manager2 = GardenManager("Bob")
    height_validation = manager1.add_plants(plants1)
    manager1.grow_plants()
    print("\n=== Alice's Garden Report ===")
    manager1.garden_report()
    print(f"\nHeight validation: {height_validation}")
    GardenManager.get_points()
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
