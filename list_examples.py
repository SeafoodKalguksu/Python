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
def sort_list_in_place(numbers: List[int], languages: List[str]) -> None:
    numbers.sort()
    numbers.sort(reverse = True)
    languages.sort(key = len)

    languages.sort(reverse = True, key = lambda lang: lang[0])
    languages.sort(key = lambda lang: (lang[0], lang[1]))
    id_list.sort(key = lambda id: id[2:])
    name_number.sort(key = lambda pair: pair[1])


def main() -> None:
    sort_list_in_place(integers, langs)


if __name__ == "__main__":
    main()
