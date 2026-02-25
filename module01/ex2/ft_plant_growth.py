
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def plant_grow(self):
        self.height += 6

    def plant_age(self):
        self.age += 6

    def get_info(self):
        print(
            self.name + ":",
            str(self.height) + "cm,",
            str(self.age) + " days old")


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
        last_height = plant.height
        plant.plant_grow()
        plant.plant_age()
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
    print("Growth this week:", "+" + str(plant.height - last_height) + "cm")


if __name__ == "__main__":
    main()
