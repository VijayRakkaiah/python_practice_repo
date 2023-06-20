s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

print(s1 | s2)  # print(s1.union(s2))

print(s1 & s2)

print(s1 - s2)

print(s2 - s1)

print(s1 ^ s2)


# FROZENSET

f = frozenset(s1)   #frozenset is immutable
