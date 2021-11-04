# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

FRUITS = 'apple#banana#cherry#orange'
WORKING_DAYS = 'Mon Tue Wed Thu Fri'
NAME = "heeseok"
INTEGERS = '123456789012345'

def string_into_list() -> None:
    # Split a string into a list.
    # Setting the maxsplit parameter to 3, will return a list with 4.
    fruits: List[str] = FRUITS.split('#', 3)
    print(f"fruits = {fruits}")

    # The default means split according to any white space,
    # and discard empty strings from the result.
    working_days: List[str] = WORKING_DAYS.split()
    print(f"working_days = {working_days}")

    # Convert a string to a list.
    name: List = list(NAME)
    print(f"name = {name}")

def list_to_string() -> None:
    # Convert a list to a string.
    capital_name: str = ''.join('HEESEOK')
    print(f"capital_name = {capital_name}")

def find_examples() -> None:
    # Return the lowest index in the string where substring sub is found.
    # str.find(sub[, start[, end]])
    index: int = INTEGERS.find('1', 3, 13)
    print(f"INTEGERS.find('1', 3, 4), index = {index}")
    index = INTEGERS.find('1')
    print(f"INTEGERS.find('1'), index = {index}")
    index = INTEGERS.find('11')
    print(f"INTEGERS.find('11'), index = {index}")
    index = INTEGERS.rfind('5')
    print(f"INTEGERS.rfind('5'), index = {index}")

def index_examples() -> None:
    # Like find(), but raise ValueError when the substring is not found.
    # str.index(sub[, start[, end]])
    index = INTEGERS.index('1')
    print(f"index = {index}")
    # index = integers.index('11')  # ValueError

def replace_example() -> None:
    # String object is immutable.
    # name[0] = 'H' wrong! using str.replace() instead of assignment.
    new_name: str = NAME.replace('h', 'H')
    print(f"new_name = {new_name}")

def reverse_examples() -> None:
    # Reverse string
    reversed_name_1: str = NAME[-1::-1]
    reversed_name_2: str = NAME[::-1]
    reversed_name_3: str = ''.join(list(reversed(list(NAME))))

    print(f"reversed_name_1 = {reversed_name_1}")
    print(f"reversed_name_2 = {reversed_name_2}")
    print(f"reversed_name_3 = {reversed_name_3}")


def main() -> None:
    string_into_list()
    list_to_string()
    find_examples()
    replace_example()
    reverse_examples()

if __name__ == "__main__":
    main()
