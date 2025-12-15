"""
{23,23,42,'ergf',True}

- {} -> empty dictionary
- .set() -> empty set
unique elements
mutable
"""

s = {1,2,3,4,5,6,7,8,9,1,2,3}
e = set()
f= {}
print(s, type(s))
print(e, type(e))
print(f, type(f))

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.union(s2)) # AUB
print(s1.intersection(s2)) # A^B
print(s1.difference(s2)) # A-B
print(s1.symmetric_difference(s2)) # (AUB)-A^B
print({1,2}.issubset(s1))
print({1,2,3,4,5,6,7,8,9}.issuperset(s1))
s1.add(7)
print(s1)

# s1.pop() -> removes a random element