'''
Write a program which prompts the user for a Celsius temperature, convert the temperature to
Fahrenheit and print out the converted temperature. Note:` ºC *9/5 +32 = ºF
'''
oC = int(input("Enter the temperature in celsius:"))

oF = oC *9/5 + 32

print("Fahrenheit: ", oF)
