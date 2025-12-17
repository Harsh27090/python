# same name different forms

# method overriding
class Bird:
    def sound(self):
        print('Bird sound')


class Crow(Bird):
    def sound(self):
        print('Crow sound')

class Parrot(Bird):
    def sound(self):
        print('Parrot sound')

bird1 = Bird()
bird2 = Crow()
bird3 = Parrot()
bird1.sound()
bird2.sound()
bird3.sound()

# python doesn't support method overloading (methods with same name in a class)

# operators
print(10+5)
print('Hello'+'World')
print([10,5]+[10,5])