"""
raise: used to manually throw an exception
"""

age = int(input("Enter your age:"))

try:
    if age<10 or age>18:
        raise ValueError("Sorry, you are not valid")
    else:
        print("Welcome to the club!")

except Exception as e:
    print(e)

print("Club will start soon!")