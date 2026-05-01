from abc import ABC, abstractmethod
import typing
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.counter: int = 0

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
        else:
            self.storage.append(str(data))


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
        else:
            self.storage.append(str(data))


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
        else:
            self.storage.append(": ".join(data.values()))


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    np_test = NumericProcessor()
    print(f" Trying to validate input '42': {np_test.validate(42)}")
    print(f" Trying to validate input 'Hello': {np_test.validate("Hello")}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np_test.ingest("foo")
    except Exception as err:
        print(f" Got exception: {err}")
    np_list_test: list[int] = [1, 2, 3, 4, 5]
    print(f" Processing data: {np_list_test}")
    print(" Extracting 3 values...")
    np_test.ingest(np_list_test)
    for _ in range(3):
        res = np_test.output()
        if res is not None:
            print(f" Numeric value {res[0]}: {res[1]}")

    print("\nTesting Text Processor...")
    tp_test = TextProcessor()
    print(f" Trying to validate input '42': {tp_test.validate(42)}")
    tp_list_test: list[str] = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {tp_list_test}")
    print(" Extracting 1 value...")
    tp_test.ingest(tp_list_test)
    res = tp_test.output()
    if res is not None:
        print(f" Text value {res[0]}: {res[1]}")

    print("\nTesting Log Processor...")
    lp_test = LongProcessor()
    print(f" Trying to validate input 'Hello': {lp_test.validate("Hello")}")
    print(" Processing data: [{'log_level': 'NOTICE', 'log_message': "
          "'Connection to server'}, {'log_level': 'ERROR', 'log_message': "
          "'Unauthorized access!!'}]")
    lp_dict_test: list[dict[str, str]] = [{'log_level': 'NOTICE',
                                           'log_message':
                                           'Connection to server'},
                                          {'log_level': 'ERROR',
                                          'log_message':
                                           'Unauthorized access!!'}]
    lp_test.ingest(lp_dict_test)
    print(" Extracting 2 values...")
    for _ in range(2):
        res = lp_test.output()
        if res is not None:
            print(f" Log entry {res[0]}: {res[1]}")


if __name__ == "__main__":
    main()
