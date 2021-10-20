# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import collections

# For loop
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


def main():
    for_loops()
    compare_id()
    compare_value()

if __name__ == "__main__":
    main()
