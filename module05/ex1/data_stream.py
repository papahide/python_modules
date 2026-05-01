from abc import ABC, abstractmethod
import typing
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.counter: int = 0
        self.processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str] | None:
        last: str = self.storage[0]
        self.storage.pop(0)
        pos: int = self.counter
        self.counter += 1
        return (pos, last)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, int | float)
                       for item in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            typed_list = typing.cast(list[int], data)
            for item in typed_list:
                self.storage.append(str(item))
                self.processed += 1
        else:
            self.storage.append(str(data))
            self.processed += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper string data")
        if isinstance(data, list):
            typed_list = typing.cast(list[str], data)
            for item in typed_list:
                self.storage.append(str(item))
                self.processed += 1
        else:
            self.storage.append(str(data))
            self.processed += 1


class LongProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and
                       isinstance(v, str)
                       for k, v in data.items())
        elif isinstance(data, list):
            return all(all(isinstance(k, str) and
                           isinstance(v, str)
                           for k, v in item.items())
                       for item in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper dictionary data")
        if isinstance(data, list):
            typed_data = typing.cast(list[dict[str, str]], data)
            for item in typed_data:
                self.storage.append(": ".join(item.values()))
                self.processed += 1
        else:
            self.storage.append(": ".join(data.values()))
            self.processed += 1


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            validation: bool = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    validation = True
                    break
            if not validation:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                print(f"{type(proc).__name__}: total "
                      f"{proc.processed} items processed, "
                      f"remaining "
                      f"{len(proc.storage)} "
                      f"on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    ds_test = DataStream()
    print("== DataStream statistics ==")
    ds_test.print_processors_stats()
    print("\nRegistering Numeric Processor")
    ds_test.register_processor(NumericProcessor())
    data: list[typing.Any] = ['Hello world', [3.14, -1, 2.71],
                              [{'log_level': 'WARNING',
                                'log_message':
                                'Telnet access! Use ssh instead'},
                               {'log_level': 'INFO',
                                'log_message': 'User wil is connected'}],
                              42, ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {data}")
    ds_test.process_stream(data)
    print("== DataStream statistics ==")
    ds_test.print_processors_stats()
    print("\nRegistering other data processors")
    ds_test.register_processor(TextProcessor())
    ds_test.register_processor(LongProcessor())
    print("Send the same batch again")
    ds_test.process_stream(data)
    print("== DataStream statistics ==")
    ds_test.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for proc in ds_test.processors:
        if type(proc).__name__ == "NumericProcessor":
            for _ in range(3):
                proc.output()
        if type(proc).__name__ == "TextProcessor":
            for _ in range(2):
                proc.output()
        if type(proc).__name__ == "LongProcessor":
            proc.output()
    print("== DataStream statistics ==")
    ds_test.print_processors_stats()


if __name__ == "__main__":
    main()
