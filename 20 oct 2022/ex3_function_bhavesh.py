'''
First, def a function called distance_from_zero, with one argument (choose any argument
name you like). If the type of the argument is either int or float, the function should return the
absolute value of the function input. Otherwise, the function should return "Nope". Check if it
works calling the function with -5.6 and "what?".
'''

import math
def distance_from_zero(d):
    if d == int or float:
        return math.fabs(d)
    else:
        return "Nope"
print(distance_from_zero(-5.6))


