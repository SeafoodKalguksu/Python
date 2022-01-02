# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import sys
import collections
from typing import Counter, List, DefaultDict, Dict, Set

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


def set_default_values_in_dictionary() -> None:
    """
    6. Define default values in Dictionaries with .get() and .setdefault()
    """
    shopping_dict = {"item": "shirt", "price": 10.00}

    def using_dict_get() -> None:
        """
        dict().get(key, default_value)
        The get() method returns the value of the item with the specified key.
        None is a default value for non-existent key of dictionary.
        """
        size = shopping_dict.get("size")
        print(size)  # None

        color = shopping_dict.get("color", "red")
        print(color)  # red

        print(shopping_dict)  # {'item': 'shirt', 'price': 10.0}

    def using_dict_setdefault() -> None:
        """
        setdefault(key[, default])
        If key is in the dictionary, return its value. If not, insert key with
        a value of default and return default. default defaults to None.
        """
        count = shopping_dict.setdefault("count", 0)
        print(count)  # 0
        print(shopping_dict)  # {'item': 'shirt', 'price': 10.0, 'count': 0}

    def using_collections_defaultdict() -> None:
        """
        Return a new dictionary-like object.
        defaultdict is a subclass of the built-in dict class.
        """
        dic: DefaultDict[str, int] = collections.defaultdict(int)
        dic["A"] = 90
        dic["B"] = 80
        dic["C"] += 1

        print(dic)  # defaultdict(<class 'int'>, {'A': 90, 'B': 80, 'C': 1})

        print("collections.defaultdict(int), dic['C']: ", dic["C"])
        # collections.defaultdict(int), dic['C']:  1

        print("collections.defaultdict(int), dic['D']: ", dic["D"])
        # collections.defaultdict(int), dic['D']:  0

        print(dic)
        # defaultdict(<class 'int'>, {'A': 90, 'B': 80, 'C': 1, 'D': 0})

    def using_key_only() -> None:
        size = shopping_dict["size"]
        print(size)
        # File "/Users/heeseok/Development/SeafoodKalguksu/Python/refactoring.py", line 91, in set_default_values_in_dictionary
        #    size = shopping_dict["size"]
        #    KeyError: 'size'

    def using_counter() -> None:
        """
        7. Count hashable objects with collections.Counter
        """
        numbers: List[int] = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9, 9]
        counter = collections.Counter(numbers)

        # Accessing a specific item.
        print(counter[10])  # 3

        # Accessing an item that does not exist in the list, 0 is returned.
        print(counter[11])  # 0

        # most_common() returns List[Tuple[element: int, count: int]]
        print(counter.most_common(3))  # [(9, 6), (10, 3), (5, 2)]

        print(counter)  # Counter({9: 6, 10: 3, 5: 2, 2: 1})

    using_dict_get()
    using_dict_setdefault()
    using_collections_defaultdict()
    using_counter()


def main() -> None:
    using_sorted()
    using_generator()
    set_default_values_in_dictionary()


if __name__ == "__main__":
    main()
