# Multiple_Func_Arg_Tst.py
# The * and ** operator to handle multiple function arguments. 
# The * operator is used to pass a list of arguments as separate positional arguments, and 
# the ** operator is used to pass a dictionary of keyword arguments.


def print_arguments(*args, **kwargs):
    print(args)
    print(kwargs)

print_arguments(1, 2, 3, name='John', age=30)

#(1, 2, 3)
#{'name': 'John', 'age': 30}














