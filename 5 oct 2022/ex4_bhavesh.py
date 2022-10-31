'''
Write a program that ask for a number to the user and classifies it:
number <2 SMALL
number <10 MEDIUM
number rest LARGE
'''

number = int(input("Enter the number:"))
if number < 2:
    print("SMALL")
elif number < 10:
    print("MEDIUM")
else:
    print("LARGE")
