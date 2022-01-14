from typing import NoReturn, Optional


class TypeNoReturn:
    """
    The typing module provides a special type NoReturn to annotate functions that never return normally.
    """

    def always_raises_exception(self) -> NoReturn:
        raise AssertionError("Why always me?")

    def loops_forever(self) -> NoReturn:
        """
        Looping forever in a function.
        """
        # On a server-sdie
        # while True:
        #     request = get_request()
        #     response(request)


class TypeNone:
    """
    Examples for a type hint 'None'
    """

    def implicitly_returns_none(self) -> None:
        """
        Python actually inserts an implicit return 'none' at the end of every function
        """
        print("has no return statement but it returns None.")

    def explicitly_returns_none(self) -> None:
        """
        Explicitly returns None like the function terminated abnormally.
        """
        return None


class TypeOptional:
    """
    Optional type
    """

    def example(self, arg: Optional[int] = None) -> NoReturn:
        pass

    def union_type_expressions(self, arg: int | None) -> NoReturn:
        pass


class TypeUnion:
    """
    To define a union, use e.g. Union[int, str] or the shorthand int | str. Using that shorthand is recommended. Details:
    """

    # union type expressions
    def square(number: int | float) -> int | float:
        return number ** 2
