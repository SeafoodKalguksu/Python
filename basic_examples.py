# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import random
import collections


def for_loops():
    string = "abcdef"
    chars = ['u', 'a', 'e', 'c', 'k', 'i']
    dic = collections.defaultdict(int)
    dic['A'] = 90
    dic['B'] = 80
    dic['C'] = 70

    for letter in string: # string
        print(letter)

    for idx, val in enumerate(chars): # list
        print(idx, val)

    for key, val in dic.items(): # dict
        print(key, val)

    for countdown in 5, 4, 3, 2, 1, 'hey!':
        print(countdown)

    for _ in range(10):
        print('hi')

    _, second_number = range(2)
    print(f'second_number == {second_number}')


# Differences between 'is' and  '=='
# Return a shallow copy of the list.
NUMBERS = [1, 2, 3]

def compare_id():
    lst = NUMBERS[:]  # NUMBERS.copy()
    if NUMBERS is lst:
        print('same id')
    else:
        print('different id')

def compare_value():
    lst = NUMBERS
    if NUMBERS == lst:
        print('same value')
    else:
        print('different value')


def print_examples():
    idx = 0
    favorite_fruit = 'apple'

    print('a', 'b', sep=', ')
    print('aa', end=' ')
    print('bb')

    print('{0}: {1}'.format(idx, favorite_fruit))
    print('{}: {}'.format(idx, favorite_fruit))
    print(f'{idx}: {favorite_fruit}')   # 3.6+


def random_exmaples():
    random.random() # -> random floating point number in the range [0.0, 1.0].
    random.uniform(1.0, 100.0)

    random.randint(1, 100)
    random.randrange(1, 100, 2) # start, stop[, step]


def main():
    for_loops()
    compare_id()
    compare_value()
    random_exmaples()

if __name__ == "__main__":
    main()
