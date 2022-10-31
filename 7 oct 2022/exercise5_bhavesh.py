
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







