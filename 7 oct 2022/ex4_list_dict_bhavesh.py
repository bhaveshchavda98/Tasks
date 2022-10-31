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
