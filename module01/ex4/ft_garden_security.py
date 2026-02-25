
class SecurePlant:
    def __init__(self, _name, _height, _age):
        self._name = _name
        self._height = _height
        self._age = _age

    def set_height(self, new_height):
        if new_height < 0:
            print("\nInvalid operation attempted: height",
                  str(new_height) + "cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print("Height updated:", str(new_height) + "cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print("\nInvalid operation attempted: age",
                  str(new_age) + "days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print("Age updated:", str(new_age) + " days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


def create_plant(_name, _height, _age):
    plant = SecurePlant(_name, _height, _age)
    return plant


def main():
    plant = create_plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created:", plant._name)
    plant.set_height(20)
    plant.set_age(30)
    plant.set_height(-5)
    print("\nCurrent plant:",
          plant._name,
          "(" + str(plant.get_height()) + "cm,",
          str(plant.get_age()) + " days" + ")")


if __name__ == "__main__":
    main()
