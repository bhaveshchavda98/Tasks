'''
Write a program to prompt for a file name, and then read through the file line-by-line. Note: the file
name is Erle.txt and its content is,
Erle is the enabling technology for the
next generation of aerial and terrestrial
robots that will be used in cities solving
tasks such as surveillance, environmental
monitoring or even providing aid at catastrophes.
Ensure you create the file.
'''
file = open('Erle.txt')

for line in file:
    print(line, end="")







