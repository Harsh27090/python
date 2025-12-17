class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello! I am {self.name}, I am a Human {self.age} years old.')

class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = 'Male'

    def desc(self):
        print(f'My name is {self.name}, my age is {self.age} and my gender is {self.gender}')

class Female(Human):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.gender = 'Female'

    def desc(self):
        print(f'My name is {self.name}, my age is {self.age} and my gender is {self.gender}')

obj1 = Human('Pujan', 21)
obj2 = Female('Khushi',20)
obj3 = Male('Harsh', 19)

obj1.greet()
obj2.greet()
obj3.greet()
obj2.desc()
obj3.desc()




