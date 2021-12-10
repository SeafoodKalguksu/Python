# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from collections import deque
from typing import Deque
import itertools

# Use deque: list-like container with fast appends and pops on either end. popleft() -> O(1)

lst = [i for i in range(10)]
mid: int = len(lst) // 2

# Can't use 'slice', an only integer is allowed in deque().
# deque(lst[0:mid]):    wrong
# deque(lst[1:]):       correct
# use itertools.islice() as follows:
first_half = deque(itertools.islice(lst, 0, mid))
second_half = deque(itertools.islice(lst, mid, len(lst)))

print(first_half)
print(second_half)
print(list(first_half))
print(list(second_half))
