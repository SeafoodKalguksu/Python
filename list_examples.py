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
    integers.append('a')
    integers.insert(2, 'b')


# Extend the list by appending elements from the iterable
def extend_iterable() -> None:
    numbers: List[int] = [9, 8, 7, 6]
    print(f'numbers = {numbers}, integers = {integers}')
    integers.extend(numbers)
    print(f'integers = {integers} after integers.extend(number)')


# Remove item from the list
def remove_item() -> None:
    integers.remove(1) # remove the first occurrence of the value

    print(integers.pop()) # remove and return item at index (default last)
    print(integers.pop(1))

    # remove all items
    # integers.clear()
    # del integers[:]
    # integers = []
    # integers[:] = []
    # integers *= 0


# Return the index of the value from the list
def get_index() -> None:
    index = integers.index(3, 2, -1) # list.index(item[, start[, end]])
    print(f'3 is at integers[{index}].')

    # Return the first index of the value from the list
    if 'a' not in integers:
        print("'a' is not in integers.")
    else:
        idx = integers.index('a')
        print(f'a is at integers[{idx}].')


# Remove non-integr elements from the list
def remove_non_integers() -> None:
    non_integer_idx = []

    for idx, item in enumerate(integers):
        # if type(item) != int:
        if not isinstance(item, int):
            print(f'item = {item}, type({item}) = {type(item)}')
            non_integer_idx.append(idx)

    for idx in non_integer_idx[::-1]:
        integers.pop(idx)

    print(f'integers = {integers} after removing non integer elements')


# Remove duplicates from the list
def remove_duplicates(lst: List[int]) -> List[int]:
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
    extend_iterable()
    remove_item()
    get_index()

    # Count the given item in the list
    print(f'integers.count(7) = {integers.count(7)}')

    remove_non_integers()
    non_duplicate_integers = remove_duplicates(integers)
    print(f'integers = {non_duplicate_integers}')

if __name__ == "__main__":
    main()
