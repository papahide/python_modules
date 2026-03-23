from typing import Generator 
import time
import random


def ft_generate_events(events: int) -> Generator[str, None, None]:
    names: list[str] = ["alice", "bob", "charlie"]
    levels: dict[str, int] = {"alice": 5, "bob": 12, "charlie": 8}
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, events + 1):
        """
        name = names[(i - 1) % len(names)]
        action = actions[(i - 1) % len(actions)]
        """
        name: str = random.choice(names)
        action: str = random.choice(actions)
        level = levels[name]

        yield f"Event {i}: Player {name} (level {level}) {action}"


def ft_fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def ft_prime_generator() -> Generator[int, None, None]:
    prime = 2
    while True:
        is_prime: bool = True
        for n in range(2, int(prime**0.5) + 1):
            if prime % n == 0:
                is_prime = False
                break

        if is_prime == True:
            yield prime

        prime += 1



def main() -> None:
    print("=== Game Data Stream Processor ===")

    print("\nProcessing 1000 game events...\n ")
    start_time = time.time()
    total = 0
    treasures = 0
    high_level = 0
    level_up = 0
    for event in ft_generate_events(1000):
        total += 1
        print(event)
        if "found treasure" in event:
            treasures += 1
        elif "leveled up" in event:
            level_up += 1
        for n in range(10, 20):
            if f"(level {n})" in event:
                high_level += 1
                break
    end_time = time.time()
    duration = end_time - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib = ft_fibonacci_generator()
    res_fib: list[str] = []
    for _ in range(10):
        res_fib.append(str(next(fib)))
    print(f"Fibonacci sequence (first 10): {", ".join(res_fib)}")
    prime = ft_prime_generator()
    res_prime: list[str] = []
    for _ in range(5):
        res_prime.append(str(next(prime)))
    print(f"Fibonacci sequence (first 10): {", ".join(res_prime)}")


if __name__ == "__main__":
    main()