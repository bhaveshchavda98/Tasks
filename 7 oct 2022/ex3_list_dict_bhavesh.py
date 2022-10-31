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
