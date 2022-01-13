from typing import NoReturn


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

    def calls_function_without_return_value(self) -> NoReturn:
        self.loops_forever()


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
