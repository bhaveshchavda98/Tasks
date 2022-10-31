'''
Rewrite your pay computation program (previous chapter) with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
hours = int(input("Enter the Hours:"))
def computepay(hours, rate):
    rate = 10
    pay1 = hours * rate
    if hours > 40:
        pay2 = (hours - 40) * (rate * 1.5 - 10)
        return pay1 + pay2
    else:
        return hours * rate
print(computepay(hours, 10))

