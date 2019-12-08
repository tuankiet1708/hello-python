# Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. We shall deal with functions for this tutorial. The syntax

# @decorator
# def functions(arg):
#     return "value"

# Is equivalent to:

# def function(arg):
#     return "value"
# function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions

# As you may have seen, a decorator is just another function which takes a functions and returns one. For example you could do this:

def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value

# This would make a function repeat twice.
@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)



# You can also make it change the output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function

# change input
def double_Ii(old_function):
    def new_function(arg): # only works if the old function has one argument
        return old_function(arg * 2) # modify the argument passed
    return new_function

# and do checking.
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

# Let's say you want to multiply the output by a variable amount. You could define the decorator and use it as follows:

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15

# You can do anything you want with the old function, even completely ignore it! Advanced decorators can also manipulate the doc string and argument number. For some snazzy decorators, go to http://wiki.python.org/moin/PythonDecoratorLibrary.