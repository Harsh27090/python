# Strings
name = "Harsh"
print(len(name)) # length of string
print(name[0])
print(name[-1])
print(name[0:3])

course = "  python \" programming"
print(course)

first = "Harsh"
last = "Chauhan"
full = f"{first} {last}"
print(full)

print(course.upper()) # string in upper case
print(course.lower()) # string in lower case
print(course.title()) # string with first letters capital
print(course.strip()) # no leading white space
print(course.find("pro"))
print(course.find("Pro"))
print(course.replace("p","j"))
print("pro" in course)
print("pro" not in course)