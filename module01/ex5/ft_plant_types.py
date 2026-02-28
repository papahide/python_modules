
class Plant:
    """
    Father Plant class
    """
    def __init__(self, name: str,
                 height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Child class that inherits from
    Plant and adds instance methods
    """
    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def get_details(self) -> None:
        print(f"{self.name}, (Flower): "
              f"{self.height}cm, {self.age} "
              f"days, {self.color} color")
        self.bloom()


class Tree(Plant):
    """
    Child class that inherits from
    Plant and adds instance methods
    """
    def __init__(
            self, name: str, height: int,
            age: int, trunk_diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides "
              f"{(self.height * self.trunk_diameter) // 320} "
              f"square meters of shade\n")

    def get_details(self) -> None:
        print(f"{self.name}, (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter} diameter")
        self.produce_shade()


class Vegetable(Plant):
    """
    Child class that inherits from
    Plant and adds instance methods
    """
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_details(self) -> None:
        print(f"{self.name}, (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")
        self.describe_nutrition()


def main():
    """
    Main func to create the object from the father
    class and the child classes to test their instance methods
    """
    plants = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    ]
    print("=== Garden Plant Types ===\n")
    for plant in plants:
        plant.get_details()


if __name__ == "__main__":
    main()
