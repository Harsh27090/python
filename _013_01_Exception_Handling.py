"""
exception: an error or uncertain event occurred during execution

try: the statements which can cause an exception are written here
except: contains what to do with the exception
else: it runs if there is no exception
finally: this always runs, no matter exception occurs or not
"""

a = int(input('Enter a no.:'))

try:
    print(10/a)

except ZeroDivisionError:
    print('ZeroDivision error occurred, you can not divide by zero!')

else:
    print('No exception occurred')

finally:
    print('I will run no matter what!')
