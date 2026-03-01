
def check_temperature(temp_str):
    """
    Checks for Value errors and checks the temperature is right.
    """
    try:
        temperature = int(temp_str)
        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temperature}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def main():
    """
    Main function that passes some arguments
    to "check_temperature" to check the outputs
    """
    temps = [25, "abc", 100, -50]
    print("=== Garden Temperature Checker ===")
    for temp in temps:
        print(f"\nTesting temperature: {temp}")
        check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
