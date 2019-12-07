# Partial functions
# You can create partial functions in python by using the partial function from the functools library.

# Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.

# Import required:
from functools import partial

# This code will return 8.
from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

# An important note: the default values will start replacing variables from the left. The 2 will replace x. y will equal 4 when dbl(4) is called. It does not make a difference in this example, but it does in the example below.