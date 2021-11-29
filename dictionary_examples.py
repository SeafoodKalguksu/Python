# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import collections
from typing import Dict, DefaultDict, List, Tuple

def dictionary() -> None:
    dic: Dict = dict(x=10, y=11) # {'x': 10, 'y': 11}
    dic = dict()
    dic['a'] = 1
    dic['b'] = 2

    # setdefault(key[, default])
    # If key is in the dictionary, return its value. If not, insert key with
    # a value of default and return default. default defaults to None.
    print(dic.setdefault('c', 3))
    dic.pop('a')
    key, value = dic.popitem() # Changed in v3.7 : LIFO order is now guaranteed
    print(f'key = {key}, value = {value}')

def default_dictionary() -> None:
    dic: DefaultDict[str, int] = collections.defaultdict(int)
    dic['A'] = 90
    dic['B'] = 80
    dic['C'] += 1
    print(dic)

def compound_dictionary() -> None:
    colors: Tuple[str, int] =  [('white', 1), ('blue', 2), ('red', 1)]
    lst: List[Tuple] = colors
    dic: DefaultDict[str, List[int]] = collections.defaultdict(list)

    lst.append(('black', 2))
    lst.append(('white', 2))
    lst.append(('blue', 4))

    for key, value  in lst:
        # dic[key] = value
        # When keys are encountered again, the look-up proceeds normally(
        # returning the list for that key) and the list.append() adds another
        # value to the list.
        dic[key].append(value)

    print(sorted(dic.items(), reverse=False))
    # [('blue', [2, 4]), ('red', [1]), ('white', [1, 2])]


def main() -> None:
    dictionary()
    default_dictionary()
    compound_dictionary()

if __name__ == "__main__":
    main()
