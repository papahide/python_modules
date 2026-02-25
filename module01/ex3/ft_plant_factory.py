
class Plant:
    """
    Plant Class
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    """
    This is tha main func used to
    create the plants more efficiently
    """
    plants = [
        ("Oxalis versicolor", 12, 43),
        ("Anguloa uniflora", 9, 16),
        ("Diphylleia grayi", 5, 7),
        ("Moriviví", 5, 23),
        ("Cuerno de Alce", 1, 1)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant = Plant(plant[0], plant[1], plant[2])
        print(
            "Created:", plant.name,
            "(" + str(plant.height) + "cm,",
            str(plant.age) + " days" + ")")
    print("\nTotal plants created:", str(len(plants)))


if __name__ == "__main__":
    main()
