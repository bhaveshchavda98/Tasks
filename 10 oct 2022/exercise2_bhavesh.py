'''
Create a variable, backwards_by_tens, and set it equal to the result of going backwards
through to_one_hundred by tens. Go ahead and print backwards_by_tens to the console.
'''
backwards_by_tens = [i for i in range(100,0,-1) if i%10==0]
print(backwards_by_tens)
