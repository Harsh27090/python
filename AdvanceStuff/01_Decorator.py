# decorator is used to decorate a function, to add some basic details

class Animal:
    @property # built-in decorator
    def show(self):
        print('I am an animal')

obj1 = Animal()
obj1.show

# 1.
def msg(func):
    def wrapper():
        print('I will run before calling function')
        func()
        print('I will run after calling function\n')

    return wrapper

@msg
def hello():
    print('Hello! I am Harsh Chauhan')


def addition(func):
    def wrapper(a,b):
        print('I will run before calling function')
        func(a,b)
        print('I will run after calling function\n')

    return wrapper

@addition
def addition(a,b):
    print(f'Addition is {a+b}')

hello()
addition(2,3)

