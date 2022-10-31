class Triangle:
    def __init__(self, angel1, angel2, angel3):
        self.angel1 = angel1
        self.angel2 = angel2
        self.angel3 = angel3

    number_of_sides = 3

    def check_angles(self):
        if (self.angel1 + self.angel2 + self.angel3) == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
