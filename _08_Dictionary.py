"""
key:value pairs
- unique keys
- value can be a single element or a list of elements
"""

my_dict ={
    'Name': 'Harsh', 'Marks': [54,32,65,34], 100: 'jnfkn'
}

print(my_dict)

# add
my_dict['Branch'] = "CS"
print(my_dict)

# update
my_dict['Marks'] = [85,64,86,85]
print(my_dict)

# remove
del my_dict[100]
print(my_dict)

# dictionary compression
squares = {x:x*x for x in range(1,11)}
print(squares)

# nested
new_dict = {
    'python': {'name': 'python', 'usecase': ['ai', 'ml', 'eda']},
    'java': {'name': 'java', 'usecase': 'app dev'}
}
print(new_dict)


a = my_dict.get('Name', 'Not found') # get values of the given key
b = my_dict.keys() # get all keys
c = my_dict.values() # get all values without keys
d = my_dict.items() # get all key:value pairs
print(a)
print(list(b))
print(list(c))
print(list(d))

# e = my_dict.pop('Branch', 'Not found') # removes given key
# print(e)
# f = my_dict.popitem() # removes the last key
# print(f)
# print(my_dict)

# my_dict.clear()

# loop
for i in my_dict:
    print(i)

for i in my_dict.values():
    print(i)

for i in my_dict.items():
    print(i)
