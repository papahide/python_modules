from typing import Generator
import random


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[list[tuple[str, str]], None, None]:
    while events:
        i: int = random.randint(0, len(events) - 1)
        print(f"Got event from list: {events[i]}")
        events.pop(i)
        yield events


def gen_event(
        players: list[str], action: list[str]
        ) -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(action))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    players: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions: list[str] = ["run", "eat", "sleep", "move",
                          "climb", "drown", "release",
                          "swim"]
    event: Generator[tuple[str, str], None, None] = gen_event(players, actions)
    for i in range(1000):
        tuple_ev: tuple[str, str] = next(event)
        name: str = tuple_ev[0]
        action: str = tuple_ev[1]
        print(f"Event {i}: Player {name} did action {action}")
    event: Generator[tuple[str, str], None, None] = gen_event(players, actions)
    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        tuple_ev = next(event)
        ten_events.append(tuple_ev)
    print(f"Built list of 10 events: {ten_events}")
    for ev in consume_event(ten_events):
        print(f"Remains in list: {ev}")


if __name__ == "__main__":
    main()
