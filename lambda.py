# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Lambda Expressions
# Small anonymous functions can be created with the lambda keyword.
# A lambda function can take any number of arguments, but can only have one expression.
def lambda_express() -> None:
    # add = lambda first, second: first + second
    # subtract = lambda first, second: first - second
    # multiply = lambda first, second: first * second
    # divide = lambda first, second: first / second
    # remainder = lambda first, second: first % second

    def add(first, second): return first + second
    def subtract(first, second): return first - second
    def multiply(first, second): return first * second
    def divide(first, second): return first / second
    def remainder(first, second): return first % second

    def calculate(first: int, second: int, func) -> int:
        return round(func(first, second), 1)

    print(calculate(1, 3, add))
    print(calculate(1, 3, subtract))
    print(calculate(1, 3, multiply))
    print(calculate(1, 3, divide))
    print(calculate(1, 3, remainder))


def main():
    lambda_express()


if __name__ == '__main__':
    main()
