
class SecurePlant:
    """
    Secure plant class that uses protected
    variables to restrict direct access to
    a object's internal state
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int) -> None:
        """
        Set height handling bad inputs
        """
        if new_height < 0:
            print("\nInvalid operation attempted: height",
                  str(new_height) + "cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print("Height updated:", str(new_height) + "cm [OK]")

    def set_age(self, new_age: int) -> None:
        """
        Set height handling bad inputs
        """
        if new_age < 0:
            print("\nInvalid operation attempted: age",
                  str(new_age) + "days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print("Age updated:", str(new_age) + " days [OK]")

    def get_name(self) -> str:
        print(self.__name)

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


def create_plant(name: str, height: int, age: int) -> SecurePlant:
    """
    Plant creator
    """
    plant = SecurePlant(name, height, age)
    return plant


def main() -> None:
    """
    Main function to display the object
    created and modifying it
    """
    plant = create_plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()}")
    plant.set_height(20)
    plant.set_age(30)
    plant.set_height(-5)
    print("\nCurrent plant:",
          plant.get_name(),
          "(" + str(plant.get_height()) + "cm,",
          str(plant.get_age()) + " days" + ")")


if __name__ == "__main__":
    main()
