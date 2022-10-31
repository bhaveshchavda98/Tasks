'''
Follow the steps:
• First, make a list called groceries with the values "banana","orange", and "apple".
• Define this two dictionaries:
stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
• Define a function compute_bill that takes one argument food as input. In the function,
create a variable total with an initial value of zero.For each item in the food list, add the
price of that item to total. Finally, return the total. Ignore whether or not the item you're
billing for is in stock.Note that your function should work for any food list.
• Make the following changes to your compute_bill function:
• While you loop through each item of food, only add the price of the item to total if
the item's stock count is greater than zero.
• If the item is in stock and after you add the price to the total, subtract one from the
item's stock count.
'''

groceries = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
food = input("Enter the food:")
def compute_bill(food):
    food_list = []
    food = food.split(' ')
    [food_list.append(n) for n in food]
    total = 0
    for i in food_list:
        price = prices[i]
        if stock[i] > 0:
            total += price
            stock[i]=stock[i]-1
    return total
print(compute_bill(food))
