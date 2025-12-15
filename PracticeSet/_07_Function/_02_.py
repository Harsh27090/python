# celsius to Fahrenheit

def fahrenheit(c):
    return (9/5)*c + 32

celsius = float(input("Enter temperature in Celsius: "))
temp = fahrenheit(celsius)
print(round(temp,2))

