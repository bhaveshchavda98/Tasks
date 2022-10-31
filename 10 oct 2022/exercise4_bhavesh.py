'''
Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension
could be useful here. Use filter() and a lambda expression to print out only the squares that are
between 30 and 70 (inclusive).
'''
squares = [i**2 for i in range(1,11)]
print(squares)

# result = filter(lambda x: x % 2 != 0, seq)
fun = lambda a: a > 30 and a <= 70

print(list(filter(fun, squares)))


