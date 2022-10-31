'''
This are the grades of some students:
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
We are going to make a function to print them.
• Define a function called print_grades() with one argument, a list called grades.
• nside the function, iterate through grades and print each item on its own line.
• After your function, call print_grades() with the grades list as the parameter.
'''
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for i in grades:
        print(i)
print_grades(grades)

