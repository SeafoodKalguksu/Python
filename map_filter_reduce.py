# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List
import functools

numbers: List[int] = [3, 1, 5, 4, 9, 11, 2]


# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# Return an iterator that applies function to every item of iterable, yielding the results.
# map(function, iterables)
def map_examples() -> None:
    # Using map() to convert float numbers to int numbers
    float_numbers: List[float] = [1.2, 2.5, 3.1, 4.0, 5.00]

    int_numbers: List[int] = list(map(int, float_numbers))
    # int_numbers = list(map(lambda number: int(number), float_numbers))
    # int_numbers = [int(number) for number in float_numbers]
    print(int_numbers)


# The filter() function returns an iterator were the items are filtered through
# a function to test if the item is accepted or not.
# filter(function, iterable)
def filter_examples() -> None:
    numbers_greater_than_5 = list(
        filter(lambda number: number > 5, numbers))
    numbers_greater_than_2 = [number for number in numbers if number > 2]

    sorted_numbers: List[int] = list(sorted(numbers))
    odd_numbers = list(filter(lambda number: number % 2 == 1, sorted_numbers))

    print(f'numbers_greater_than_5 = {numbers_greater_than_5}')
    print(f'numbers_greater_than_2 = {numbers_greater_than_2}')
    print(f'odd_numbers = {odd_numbers}')


# Using List/Dictionary comprehension instead of map() or filter()
def recommended() -> None:
    multiply_odd_num_by_2: List[int] = [
        number*2 for number in numbers if number % 2 == 1]

    dic_numbers = {key: val for key, val in enumerate(numbers)}

    print(f'numbers = {numbers}')
    print(f'multiply_odd_num_by_2 = {multiply_odd_num_by_2}')
    print(f'dic_numbers = {dic_numbers}')


# functools.reduce(function, iterable[, initializer])
def reduce_example() -> None:
    # Using reduce() to compute sum of numbers.
    accumulation_of_numbers: int = functools.reduce(
        lambda x, y: x + y, numbers)

    # Using reduce() to accumulate from 1 to 10.
    accumulation_from_1_to_10: int = functools.reduce(
        lambda x, y: x + y, range(1, 11))

    # Using reduce to compute maximum element from list
    max_in_numbers: int = functools.reduce(
        lambda prev, cur: prev if prev > cur else cur, numbers)

    # Append cur string to prev string
    langs = ['Korean', 'Japanese', 'Chinese', 'Spanish']
    result: str = functools.reduce(lambda prev, cur: prev + ', ' + cur, langs)

    print(f'accumulation_of_numbers = {accumulation_of_numbers}')
    print(f'accumulation_from_1_to_10 = {accumulation_from_1_to_10}')
    print(f'max_in_numbers = {max_in_numbers}')
    print(f'result = {result}')


def main():
    map_examples()
    filter_examples()
    recommended()
    reduce_example()


if __name__ == "__main__":
    main()
