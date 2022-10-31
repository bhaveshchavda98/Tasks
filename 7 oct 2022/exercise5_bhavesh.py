'''
Let's use functions to calculate your trip's costs:
• Define a function called hotel_cost with one argument nights as input. The hotel
costs $140 per night. So, the function hotel_cost should return 140 * nights.
• Define a function called plane_ride_cost that takes a string, city, as input. The
function should return a different price depending on the location, similar to the code
example above. Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475
-Below your existing code, define a function called rental_car_cost with an argument
called days. Calculate the cost of renting the car: Every day you rent the car costs $40.
(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50).
Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You
cannot get both of the above discounts. Return that cost. -Then, define a function
called trip_cost that takes two arguments, city and days. Like the example above,
have your function return the sum of calling
the rental_car_cost(days), hotel_cost(days),
and plane_ride_cost(city) functions.
• Modify your trip_cost function definition. Add a third argument, spending_money.
Modify what the trip_cost function does. Add the variable `spending_money to the sum
that it returns.
'''
nights = int(input("Enter the nights:"))
def hotel_cost(nights):
    costs = 140
    return costs * nights
print(hotel_cost(nights))

city = input("Enter the city:")
def plane_ride_cost():
    cities = {"Charlotte": 183, "Tampa": 220, "Pittsburgh": 222, "Los Angeles": 475}

    if city in cities:
        return cities[city]
print(plane_ride_cost())


days = int(input("Enter the Days:"))
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
        return cost
    elif days >= 3:
        cost = cost - 20
        return cost
    else:
        return cost

print(rental_car_cost(days))

spending_money = int(input("Enter spending Money:"))
def trip_cost(city, days, spending_money):
    return hotel_cost(nights) + plane_ride_cost() + rental_car_cost(days) + spending_money

print("Total Cost: ",trip_cost(city,days, spending_money))







