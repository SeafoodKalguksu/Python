# Truth Value Testing
"""
Any object can be tested for truth value, for use in an if or while condition
or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a
__bool__() method that returns False or a __len__() method that returns zero
when called with the object. Here are most of the built-in objects considered
false:

▲ constants defined to be false: None and False.
▲ zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
▲ empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)
"""

# Boolean Operations — and, or, not
"""
These are the Boolean operations, ordered by ascending priority:

Operation   Result                                          Notes
x or y      if x is false, then y, else x                   (1)
x and y     if x is false, then x, else y                   (2)
not x       if x is false, then True, else False            (3)

Notes:
1. This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
2. This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
3. not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.
"""

# Comparisons
"""
There are eight comparison operations in Python. They all have the same priority (which is higher than that of the Boolean operations). Comparisons can be chained arbitrarily; for example, x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

This table summarizes the comparison operations:

Operation   Meaning
<           strictly less than
<=          less than or equal
>           strictly greater than
>=          greater than or equal
==          equal
!=          not equal
is          object identity
is not      negated object identity
"""
