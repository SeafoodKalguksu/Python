# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import random
import collections
from typing import DefaultDict, List


def for_loops() -> None:
    string: str = "abcdef"
    chars: List[str] = ["u", "a", "e", "c", "k", "i"]
    dic: DefaultDict[str, int] = collections.defaultdict(int)
    dic["A"] = 90
    dic["B"] = 80
    dic["C"] = 70

    def for_str() -> None:
        letter: str = None

        for letter in string:  # string
            print(letter)

    def for_list() -> None:
        idx: int = None
        list_val: str = None

        for letter in chars:  # list
            print(f"letter = {letter}")

        for idx, list_val in enumerate(chars):  # list
            print(f"idx = {idx}, list_val = {list_val}")

    def for_dict() -> None:
        grade_key: str = None
        grade_val: int = None

        for grade_key, grade_val in dic.items():  # dict
            print(grade_key, grade_val)

    def for_etc() -> None:
        countdown: int = None
        for countdown in 5, 4, 3, 2, 1, "hey!":
            print(countdown)

        for _ in range(10):
            print("hi")

        second_number: int = None
        _, second_number = range(2)
        print(f"second_number == {second_number}")


# Differences between 'is' and  '=='
NUMBERS = [1, 2, 3]


def compare_id() -> None:
    numbers: List = NUMBERS[:]  # deep copy
    print("same id") if NUMBERS is numbers else print("different id")


def compare_value() -> None:
    numbers: List = NUMBERS  # shallow copy
    print("same value") if NUMBERS == numbers else print("different value")


def print_examples() -> None:
    idx: int = 0
    favorite_fruit: str = "apple"

    print("a", "b", sep=", ")
    print("aa", end=" ")
    print("bb")

    print("{0}: {1}".format(idx, favorite_fruit))
    print("{}: {}".format(idx, favorite_fruit))
    print(f"{idx}: {favorite_fruit}")  # 3.6+


def random_exmaples() -> None:
    random.random()  # -> random floating point number in the range [0.0, 1.0].
    random.uniform(1.0, 100.0)

    random.randint(1, 100)
    random.randrange(1, 100, 2)  # start, stop[, step]


# Counter object
def counter() -> None:
    lst: List[str] = ["a", "b", "c", "d", "e", "e", "f", "f", "e"]
    string: str = "abcdeabcdabcaba"

    count_alphabets = collections.Counter(lst)
    most_common_alphabets = collections.Counter(string).most_common(2)
    print(f"count alphabets in lst = {count_alphabets}")
    # Counter({'e': 3, 'f': 2, 'a': 1, 'b': 1, 'c': 1, 'd': 1})
    print(f"most common alphabets(2) in string = {most_common_alphabets}")
    # [('a', 5), ('b', 4)]


def main() -> None:
    for_loops()
    compare_id()
    compare_value()
    random_exmaples()
    counter()


if __name__ == "__main__":
    main()
