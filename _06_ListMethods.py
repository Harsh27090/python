lst = [1,2,3]
print("lst :", lst)

lst2 = lst.copy()
print("lst 2:",lst2)
print()

lst.append(4)
print(lst)

lst.extend(lst2)
print(lst)

lst.insert(3,4)
print(lst)

lst.remove(4) # removes by data
print(lst)

lst.pop(0) # removes by index
print(lst)

# lst.clear()
# print(lst)

print(lst.index(4))

print(lst.count(2))

lst.sort()
print(lst)

lst.reverse()
print(lst)

print(min(lst))
print(max(lst))

print("lst:",lst)
print("lst2:",lst2)

# common elements
s1 = set(lst)
s2 = set(lst2)
s3 = s1.intersection(s2)
print("Common elements:",list(s3))

# range
a = list(range(1,20,2))
print(a)

# list compression
squares = [i**2 for i in range(1,11,2) if i%2==0]
print(squares)
