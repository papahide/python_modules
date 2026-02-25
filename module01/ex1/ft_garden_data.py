
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    plants = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(
            plant.name + ":",
            str(plant.height) + "cm,",
            str(plant.age) + " days old")


if __name__ == "__main__":
    main()
