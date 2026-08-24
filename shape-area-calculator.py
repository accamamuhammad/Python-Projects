# Shape Area Calculator

import math

status = False

#* Parent Class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print('Area not defined for generic shape')

    def describe(self):
        print('\n')
        print(f'{self.name} has an area of {self.area():.2f}')

# 1. Cube
class Cube(Shape):
    def __init__(self, width, length, height):
       super().__init__('Cube')
       self.width = width
       self.length = length
       self.height = height

    def area(self):
        return int(self.width) * int(self.length) *  int(self.height)

# 2. Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

# 3. Rectangle
class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__('Rectangle')
        self.width = width
        self.length = length

    def area(self):
        return int(self.width) * int(self.length)


#* start loop
while not status:
    print('List of all shapes')
    print('1. Cube')
    print('2. Cricle')
    print('3. Rectangle')
    print('\n')
    user_input = input('Select shape numbered 1 - 3: ')
    print('\n')

    #& state of validation
    user_validation = False

    while not user_validation:
        if user_input not in ['1', '2', '3']:
            user_input = input('Please Select from options above 1 - 3: ')
            print('\n')
        else:
            user_validation = True
            if user_validation:
                if user_input == '1':
                    # Cube
                    width = input('Enter Width of Cube: ')
                    length = input('Enter Length of Cube: ')
                    height = input('Enter Height of Cube: ')
                    cube = Cube(width, length, height)
                    cube.describe()
                elif user_input == '2':
                    # Circle
                    radius = float(input("Enter Radius of Circle: "))
                    circle = Circle(radius)
                    circle.describe()
                elif user_input == '3':
                    # Rectangle
                    width = input('Enter Width of Rectangle: ')
                    length = input('Enter Length of Rectangle: ')
                    rectangle = Rectangle(width, length)
                    rectangle.describe()

