prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3
          }
total = 0
for i in prices:
    print(i)
    print("price:", prices[i])
    stock = int(input("Enter the stock:"))
    total = total + (stock * prices[i])
print()
print("Total:", total)