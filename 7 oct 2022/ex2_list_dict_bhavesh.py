'''
Follow the steps bellow: -Create a new dictionary called prices using {} format like the example
above.
• Put these values in your prices dictionary:
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
• Loop through each key in prices. For each key, print out the key along with its price and
stock information. Print the answer in the following format:
apple
price: 2
stock: 0
• Let's determine how much money you would make if you sold all of your food.
• Create a variable called total and set it to zero.
• Loop through the prices dictionaries.For each key in prices, multiply the number in
prices by the number in stock. Print that value into the console and then add it to
total.
• Finally, outside your loop, print total.
'''
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