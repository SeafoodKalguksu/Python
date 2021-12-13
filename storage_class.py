# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Storage class
# https://www.geeksforgeeks.org/storage-classes-in-c-with-examples/
def manipulate_global_variable():
    global variable  # in order to access the variable in global scope.
    variable = 11


def outer_func():
    variable = 12  # declared as a local variable in outer_func().
    print("local variable = ", variable)

    def inner_func():
        nonlocal variable  # in order to access the variable in outer_func().
        variable = 13

    inner_func()
    print("after inner_func() = ", variable)


variable: int = 10  # declared as a global variable
print("golbal variable = ", variable)
manipulate_global_variable()
print("after manipulate_global_variable() = ", variable)
outer_func()
print(f'gloval variable = {variable}')
