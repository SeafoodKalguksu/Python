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

def main():
    for_loops()

if __name__ == "__main__":
    main()
