# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Storage class
# https://www.geeksforgeeks.org/storage-classes-in-c-with-examples/
def manipulate_global_variable_in_func():
    global x
    x = 11

def func():
    x = 12
    print("local x = ", x)

    def func_in_func():
        nonlocal x
        x = 13

    func_in_func()
    print("after func_in_func() = ", x)

x: int = 10
print("golbal x = ", x)
manipulate_global_variable_in_func()
print("after manipulate_global_variable_in_func() = ", x)
func()
print(f'gloval x = {x}')
