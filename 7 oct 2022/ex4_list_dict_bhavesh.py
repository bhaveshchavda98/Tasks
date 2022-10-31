'''
This exercise is a bit more complicate. We will review all about list and dictionaries. The aim of this
exercise is to make a gradebook for teacher's students.
Try to follow the steps:
• Create three dictionaries: lloyd, alice, and tyler.
• Give each dictionary the keys "name", "homework", "quizzes", and "tests".Have the "name"
key be the name of the student (that is, lloyd's name should be "Lloyd") and the other keys
should be an empty list. Look in solutions, the "solution 1". Chechk if you have done it
rigth.
• Now copy this code:
lloyd = {
"name": "Lloyd",
"homework": [90.0,97.0,75.0,92.0],
"quizzes": [88.0,40.0,94.0],
"tests": [75.0,90.0]
}
alice = {
"name": "Alice",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}
tyler = {
"name": "Tyler",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}
• Below your code, create a list called students that contains lloyd, alice, and `tyler.
• for each student in your students list, print out that student's data, as follows:
• print the student's name
• print the student's homework
• print the student's quizzes
• print the student's tests
• Write a function average that takes a list of numbers and returns the average.
• Define a function called average that has one argument, numbers.
• Inside that function, call the built-in sum() function with the numbers list as a
parameter. Store the result in a variable called total.
• Use float() to convert total and store the result in total.
• Divide total by the length of the numbers list. Use the built-in len() function to
calculate that.
• Return that result.
• Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler)
as input and returns his/her weighted average.
• Define a function called get_average that takes one argument called student.TechUltra Solutions Pvt. Ltd.
• Make a variable homework that stores the average() of student["homework"].
• Repeat step 2 for "quizzes" and "tests".
• Multiply the 3 averages by their weights and return the sum of those three.
Homework is 10%, quizzes are 30% and tests are 60%.
• Define a new function called get_letter_grade that has one argument called score.
Expect score to be a number.
• Inside your function, test score using a chain of if: / elif: / else: statements, like so:
If score is 90 or above: return "A"
Else if score is 80 or above: return "B"
Else if score is 70 or above: return "C"
Else if score is 60 or above: return "D"
Otherwise: return "F"
• Finally, test your function. Call your get_letter_grade function with the result
of get_average(lloyd). Print the resulting letter grade.
• Define a function called get_class_average that has one argument, students. You can
expect students to be a list containing your three students.
• First, make an empty list called results.
• For each student item in the class list, calculate get_average(student) and then call
results.append() with that result.
• Finally, return the result of calling average() with results.
• Finally, print out the result of calling get_class_averagewith your students list. Your
students should be [lloyd, alice, tyler].
• Then, print the result of get_letter_grade for the class's average.
'''

lloyd = {"name": "Lloyd",
         "homework": [90.0, 97.0, 75.0, 92.0],
         "quizzes": [88.0, 40.0, 94.0],
         "tests": [75.0, 90.0]
         }
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

student = [lloyd, alice, tyler]

for i in student:
    print('================================')
    print("Student Name:", i['name'])
    print('Student Homework:', i['homework'])
    print('Student quizzes:', i['quizzes'])
    print('Student tests:', i['tests'])
    print('================================')


def average():
    number = [1, 2, 3, 4, 5]
    return sum(number)/3

def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)


def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return (homework*0.1)+(quizzes*0.3)+(tests*0.6)


def get_letter_grade(score):
    grade = ''
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
print(get_letter_grade(get_average(lloyd)))

def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)
print(get_class_average(student))

print(get_letter_grade(get_class_average(student)))
