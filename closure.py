# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Closures are inner functions that are enclosed within the outer function.
# Closures can access variables present in the outer function scope.
# It can access these variables even after the outer function has completed its execution.

from typing import Callable, Dict


def counter(is_plus: bool = True, start: int = 0) -> Callable:
    value: int = start

    def inc():
        nonlocal value
        value += 1
        print(f'value = {value} after inc()')

    def dec():
        nonlocal value
        value -= 1
        print(f'value = {value} after dec()')

    return inc if is_plus else dec


def accumulater(start: int = 0) -> Callable:
    accmulation: int = start

    def acc(number: int) -> int:
        nonlocal accmulation

        accmulation += number
        return accmulation

    return acc


def factorial_example() -> None:
    def factorial(number: int) -> int:
        if number is 0 or number is 1:
            return 1
        else:
            return number * factorial(number - 1)

    def memoization(factorial: Callable) -> Callable:
        cache: Dict[int] = {}

        def in_cache(number: int) -> int:
            if number in cache:
                return cache[number]
            else:
                cache[number] = factorial(number)
                return cache[number]

        return in_cache

    get_factorial_number = memoization(factorial)
    print(get_factorial_number(3))
    print(get_factorial_number(5))


def main():
    increase = counter(True, 0)
    descrease = counter(False, 0)
    increase()
    increase()
    descrease()
    descrease()

    accumulate = accumulater(5)
    accumulate(1)
    accumulate(2)
    accumulate(3)
    print(accumulate(5))

    factorial_example()


if __name__ == '__main__':
    main()
