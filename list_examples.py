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

def sort_in_place(numbers: List[int], languages: List[str]) -> None:
    # Sort the items of the list in place.
    numbers.sort()
    numbers.sort(reverse = True)
    languages.sort(key = len)

    languages.sort(reverse = True, key = lambda lang: lang[0])
    languages.sort(key = lambda lang: (lang[0], lang[1]))
    id_list.sort(key = lambda id: id[2:])
    name_number.sort(key = lambda pair: pair[1])

def new_sorted_list() -> None:
    # Return a new sorted list from the items in iterable.
    new_letters: List[str] = sorted(letters, reverse=True)
    print(f'letters = {letters}, new letters = {new_letters}')

    new_langs: List[str] = sorted(langs, key = lambda lang: lang[0])
    print(f'langs = {langs}, new langs = {new_langs} by Alphabet order')
    print(f'langs = {langs}, new langs = {sorted(langs, key = str.lower)} by lower str')

def reverse_in_place() -> None:
    # Reverse a list
    print(f'integers = {integers}', end = ', ')
    # Reverse the list in place
    integers.reverse()
    print(f'reverse integers = {integers}')

def new_reversed_list() -> None:
    # reversed(): Return a reverse iterator
    print(f'integers = {integers}, reversed integer = {list(reversed(integers))}')

def add_item() -> None:
    # Add an item in the list
    integers.append(1)  # (obj)
    integers.append('1')
    integers.insert(2, '2') # (idx, obj)
    integers.insert(2, 2)
    integers.append('a')
    integers.insert(2, 'b')

def remove_item() -> None:
    # Remove item from the list
    integers.remove(1) # remove the first occurrence of the value
    print(integers.pop()) # remove and return item at index (default last)
    print(integers.pop(1))

    # remove all items
    # integers.clear()
    # del integers[:]
    # integers = []
    # integers[:] = []
    # integers *= 0

def extend_iterable() -> None:
    # Extend the list by appending elements from the iterable
    numbers: List[int] = [9, 8, 7, 6]
    print(f'numbers = {numbers}, integers = {integers}')
    integers.extend(numbers)
    print(f'integers = {integers} after integers.extend(number)')

def get_index() -> None:
    # Return the index of the value from the list
    # list.index(item[, start[, end]])
    index = integers.index(3, 2, -1)
    print(f'3 is at integers[{index}].')

    # Return the first index of the value from the list
    if 'a' not in integers:
        print("'a' is not in integers.")
    else:
        idx = integers.index('a')
        print(f'a is at integers[{idx}].')

def count_item() -> None:
    # Count the given item in the list
    print(f'integers.count(5) = {integers.count(5)}')

def remove_non_integers() -> None:
    # Remove non-integr elements from the list
    non_integer_idx = []

    for idx, item in enumerate(integers):
        # if type(item) != int:
        if not isinstance(item, int):
            print(f'item = {item}, type({item}) = {type(item)}')
            non_integer_idx.append(idx)

    for idx in non_integer_idx[::-1]:
        integers.pop(idx)

    print(f'integers = {integers} after removing non integer elements')

def remove_duplicates(lst: List[int]) -> List[int]:
    # Remove duplicates from the list

    # O(n²)
    # non_duplicates: List = []

    # for item in lst: # O(n)
    #     if item not in non_duplicates: # O(n)
    #         non_duplicates.append(item)

    # dict.fromkeys() is much faster than using for looping. O(n) x O(1)
    return list(dict.fromkeys(lst))


def main() -> None:
    new_sorted_list()
    sort_in_place(integers, langs)

    reverse_in_place()
    new_reversed_list()

    add_item()
    remove_item()
    extend_iterable()
    get_index()
    count_item()

    remove_non_integers()
    non_duplicate_integers = remove_duplicates(integers)
    print(f'integers = {non_duplicate_integers}')

if __name__ == "__main__":
    main()
