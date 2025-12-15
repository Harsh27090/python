# for loop:

for number in range(3):
    print(number)

print()

for number in range(1,4):
    print(number, number * ".")

print()

for number in range(1, 10, 2):
    print(number, number * ".")

print()

# for else loop

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Not Successful")

print()

# Nested loops

for x in range(2):
    for y in range(3):
        print(f"{x},{y}")

print()

# while loop
number = 100
while number > 0:
    print(number)
    number //= 2

print()

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

print()

# infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
count = 0
for number in range(1,10):
    if number%2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")