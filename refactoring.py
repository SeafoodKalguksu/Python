# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import sys
from typing import List, Dict, Set

RANGE: int = 0
ENUMERATE: int = 1
FOR_LOOP: int = 2
LIST_COMPREHENSION: int = 3


def using_enumerate(select: int = ENUMERATE) -> None:
    """
    1. Iterate with enumerate() instead of range(len())
    """
    data: List[int] = [1, 2, -4, -3]

    def for_in_range() -> None:
        for index in range(len(data)):
            if data[index] < 0:
                data[index] = 0

    def for_in_enumerate() -> None:
        for index, element in enumerate(data):
            if element < 0:
                data[index] = 0

    for_in_enumerate() if select == ENUMERATE else for_in_range()


def using_list_comprehension(select: int = LIST_COMPREHENSION) -> None:
    """
    2. Use list comprehension instead of for raw loop
    """
    squares_1: List[int] = []
    squares_2: List[int] = []

    for index in range(10):
        squares_1.append(index * index)

    squares_2 = [index * index for index in range(10)]


def using_sorted() -> None:
    """
    3.Sort complex iterables with sorted()
    """
    list_data: List[int] = [3, 5, 1, 10, 9]
    tuple_data: List[int] = (3, 5, 1, 10, 9)
    complex_data: List[Dict] = [
        {"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9},
    ]

    print(sorted(list_data))  # [1, 3, 5, 9, 10]
    print(sorted(tuple_data))  # [1, 3, 5, 9, 10]
    print(sorted(complex_data, key=lambda element: element["age"]))


def using_set() -> None:
    """
    4. store unique values with set()
    """
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 7, 7]
    unique_numbers: Set[int] = set(numbers)
    print(unique_numbers)


def using_generator() -> None:
    """
    5. Save memory with generators
    """
    numbers_list = [number for number in range(10000)]  # 85176 bytes
    print(sum(numbers_list))
    print(sys.getsizeof(numbers_list), "bytes")

    numbers_generator = (number for number in range(10000))  # 104 bytes
    print(sum(numbers_generator))
    print(sys.getsizeof(numbers_generator), "bytes")


def main() -> None:
    using_sorted()
    using_generator()


if __name__ == "__main__":
    main()
