'''
Follow the steps:
• First, def a function called cube that takes an argument called number.
• Make that function return the cube of that number (i.e. that number multiplied by itself and
multiplied by itself once again).
• Define a second function called by_three that takes an argument called number. if that
number is divisible by 3,by_three should call cube(number) and return its result.
Otherwise, by_three should return False. -Check if it works.
'''
number = int(input("Enter the number:"))


def cube(number):
    return number * number * number


def by_three(number):
    if (number % 3) == 0:
        return cube(number)
    else:
        return False


print(by_three(number))
