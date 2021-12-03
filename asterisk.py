# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List, Tuple
from functools import reduce

# There are 4 cases for using the asterisk in Python.

# 1. multiplication and power operations.
def power_operation() -> None:
    mul: int = 2 * 3  # 6
    power: int = 2 ** 3  # 2³

# 2. repeatedly extending the list-type containers.
def extend_list() -> None:
    zeros_lst: List[int] = [0] * 5 # [0, 0, 0, 0, 0]
    zero_tup: Tuple[int] = (0,) * 5 # (0, 0, 0, 0, 0)
    vector: List[List[int]] = [[1, 2, 3]]
    print(vector * 3) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# 3. using the variadic arguments. (so-called “packing”)
def variadic_arguments() -> None:
    # *args(positional arguments): tuple
    # **kwargs(keyword arguments): dict
    def save_ranking(*args, **kwargs):
        print(args)
        print(kwargs)

# 4. unpacking the containers.
def unpack() -> None:
    prime_numbers = [2, 3, 5, 7, 11, 13]
    numbers = [1, 2, 3, 4, 5, 6]

    # left side should be a tuple or a list.
    *a, = numbers  # a = [1, 2, 3, 4, 5, 6]
    *a, b = numbers  # a = [1, 2, 3, 4, 5],  b = 6
    a, *b, = numbers  # a = 1, b = [2, 3, 4, 5, 6]
    a, *b, c = numbers  # a = 1, b = [2, 3, 4, 5], c = 6

    def product(*numbers):
        return reduce(lambda x, y: x * y, numbers)

    product(*prime_numbers)    # 30030
    product(prime_numbers)     # an only argument [2, 3, 5, 7, 11, 13]
