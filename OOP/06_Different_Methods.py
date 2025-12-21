class Person:
    count = 0
    def __init__(self,name,age=0):
        self.name = name
        self.age = age
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def addition(a,b):
        return a+b

obj1 = Person('Harsh',21)
obj2 = Person('Pujan', 19)
print(Person.addition(4,2))
print(obj1.count)
print(Person.get_count())

