class Animal:
    @property
    def show(self):
        print('I am an animal')

obj1 = Animal()
obj1.show

def decorate(func):
    def wrapper():
        print('I will run before calling function')
        func()
        print('I will run after calling function')

    return wrapper

@decorate
def hello():
    print('Hello! I am Harsh Chauhan')

hello()

def decorate(func):
    def wrapper(a,b):
        print('I will run before calling function')
        func(a,b)
        print('I will run after calling function')

    return wrapper

@decorate
def addition(a,b):
    print(f'Addition is {a+b}')

addition(2,3)
