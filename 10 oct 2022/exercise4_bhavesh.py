squares = [i**2 for i in range(1,11)]
print(squares)

# result = filter(lambda x: x % 2 != 0, seq)
fun = lambda a: a > 30 and a <= 70

print(list(filter(fun, squares)))


