'''
Exercise 2
You've finished eating at a restaurant, and received this bill:
Cost of meal: $44.50
Restaurant tax: 6.75%
Tip: 15%
You'll apply the tip to the overall cost of the meal (including tax).
Steps to follow:
• First, let's declare the variable meal and assign it the value 44.50.
• Now let's create a variable for the tax percentage: The tax on your receipt is 6.75%. You'll
have to divide 6.75 by 100 in order to get the decimal form of the percentage. Create the
variable tax and set it equal to the decimal value of 6.75%.
• You received good service, so you'd like to leave a 15% tip on top of the cost of the meal,
including tax. Before we compute the tip for your bill, let's set a variable for the tip. Again,
we need to get the decimal form of the tip, so we divide 15.0 by 100. Set the variable tip to
decimal value of 15% .
• Reassign in a Single Line We've got the three variables we need to perform our calculation,
and we know some arithmetic operators that can help us out. (We saw in 3.3 Variables that
we can reassign variables. For example, we could say spam = 7, then later change our minds
and say spam = 3.) Reassign meal to the value of itself + itself * tax.
• We're only calculating the cost of meal and tax here. We'll get to the tip soon. Let's introduce
on new variable, total, equal to the new meal + meal * tip.
• Insert at the end this code `print("%.2f" % total). This code print to the console the value of
total with exactly two numbers after the decimal.
'''
meal = 44.50
tax =meal * 0.0675  # 3.00375
tip = meal * (15/100)   # 6.675

total = meal + tax + tip

print("Total amount:",total)
