'''
Create a file called new_world.txt.First add a new line to the file:Welcome to robotics
time. And then print the content of new_world.txt.
'''
file = open('new_world.txt')

print("Welcome to robotics time.")
for line in file:
    print(line, end="")
