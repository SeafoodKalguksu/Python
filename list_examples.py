# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List, Tuple


integers: List[int] = [1, 2, 5, 4, 7, 3]
letters: List[str] = ['u', 'a', 'e', 'c', 'k', 'i']
langs: List[str] = ['Korean', 'Swedish', 'Japanese', 'Chinese', 'Spanish']
langs_tuple: Tuple[str] = ('English', 'German')
id_list: List = ['id01', 'id07', 'id02', 'id12', 'id03']
name_number: List[Tuple[str, int]] = [('Jake', 8), ('Sam', 3), ('Mark', 1), ('Jack', 5)]
duplicates: List[str] = ['a', 'b', 'a', 'c', 'c', 'a', 'b', 'a', 'c', 'c', 'a',
              'b', 'a', 'c', 'c', 'a', 'b', 'a', 'c', 'c', 1, 2, 5, 4, 7, 3, 'u', 'a', 'e', 'c', 'k', 'i', 'Korean', 'Japanese', 'Chinese', 'Spanish', 'English', 'German', 'Korean', 'Japanese', 'Chinese', 'Spanish']


# Sort the items of the list in place.
def sort_in_place(numbers: List[int], languages: List[str]) -> None:
    numbers.sort()
    numbers.sort(reverse = True)
    languages.sort(key = len)

    languages.sort(reverse = True, key = lambda lang: lang[0])
    languages.sort(key = lambda lang: (lang[0], lang[1]))
    id_list.sort(key = lambda id: id[2:])
    name_number.sort(key = lambda pair: pair[1])

# Return a new sorted list from the items in iterable.
def new_sorted_list() -> None:
    new_letters: List[str] = sorted(letters, reverse=True)
    print(f'letters = {letters}, new letters = {new_letters}')

    new_langs: List[str] = sorted(langs, key = lambda lang: lang[0])
    print(f'langs = {langs}, new langs = {new_langs} by Alphabet order')
    print(f'langs = {langs}, new langs = {sorted(langs, key = str.lower)} by lower str')

# Reverse a list
def reverse_in_place() -> None:
    print(f'integers = {integers}', end = ', ')
    integers.reverse()
    print(f'reverse integers = {integers}')

def new_reversed_list() -> None:
    # reversed(): Return a reverse iterator
    print(f'integers = {integers}, reversed integer = {list(reversed(integers))}')


# Add an item in the list
def add_item() -> None:
    integers.append(1)  # (obj)
    integers.append('1')
    integers.insert(2, '2') # (idx, obj)
    integers.insert(2, 2)


def main() -> None:
    new_sorted_list()
    sort_in_place(integers, langs)

    reverse_in_place()
    new_reversed_list()

    add_item()

if __name__ == "__main__":
    main()
