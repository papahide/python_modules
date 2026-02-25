
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")

    def get_details(self):
        print(f"{self.name}, (Flower): {self.height}cm, " \
              f"{self.age} days, {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides " \
              f"{(self.height * self.trunk_diameter) // 320} square meters of shade\n")

    def get_details(self):
        print(f"{self.name}, (Tree): {self.height}cm, " \
              f"{self.age} days, {self.trunk_diameter} diameter")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_details(self):
        print(f"{self.name}, (Vegetable): {self.height}cm, " \
              f"{self.age} days, {self.harvest_season} harvest")
        self.describe_nutrition()


def main():
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