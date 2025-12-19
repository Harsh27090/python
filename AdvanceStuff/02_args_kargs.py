"""
args: it is used for multiple positional arguments
it makes a tuple
syntax:
*<var_name>
"""
def addition(*args):
    sum = 0
    for i in args:
        sum += i

    return sum


print(f"Addition is {addition(1,2,3,4,5)} \n")

"""
kwargs: it used for keyword (key:value) (non-positional) arguments
it makes a dictionary
**<var_name>
"""
def information(**kwargs):
    for i in kwargs:
        print(f'{i} : {kwargs[i]}')

information(name = 'Harsh', age=21, city='Surat')

# using in decorator

def decorator_add(func):
    def wrapper(*args,**kwargs):
        print('Starting calculation')
        func(*args,**kwargs)
        print('Calculation done! Thank you!')
    return wrapper

@decorator_add
def addition(*args):
    print(f'Addition is {sum(args)}')

# @decorator_add
# def addition(*args, **kwargs):
#     print(f'Addition is {sum(args) + sum(kwargs.values())}')
# for handling calculation of positional with key word arguments

addition(1,2,3,4,5)

def decorator_info(func):
    def wrapper(*args,**kwargs):
        print('Welcome!')
        func(*args,**kwargs)
        print('Thank you!')
    return wrapper
