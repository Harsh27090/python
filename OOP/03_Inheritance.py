class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def greet(self):
        print('Hello!')

Stud1 = Student('James', 1)
Stud1.greet()