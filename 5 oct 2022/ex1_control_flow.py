'''
Write a program to prompt the user for hours and rate per hour to compute gross pay.Take into
account that the factory gives the employee 1.5 times the hourly rate for hours worked above 40
hours.
Enter Hours: 45
Rate: 10
Pay: 475.0
'''

hours = int(input("Enter the hours:"))
rate = 10
pay = hours * rate
if hours > 40:
    rate = rate*1.5
    pay = (hours-40)*rate
    rate=10
    pay = pay + 40*rate
else:
    pay = hours * rate
print("Gross Pay:", pay)

'''
hours = int(input("Hours="))
rate = 10
pay1 = hours * rate
if hours > 40:
    rate = rate * 1.5 - 10
    pay2 = (hours - 40) * rate
else:
    rate = 10
pay = pay1 + pay2
print("Gross Pay = ", pay)
'''
