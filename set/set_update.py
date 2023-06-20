s = {10 ,20, 30}
l = [5, 15, 25]

s.update(l)     #iterable datatypes
print(s)

s = {10 ,20, 30}
l = [5, 15, 25]

s.update(l, range(1,4))   #iterable datatypes
print(s)

s = {10 ,20, 30}
l = [5, 15, 25]
t = (11, 22, 33)

s.update(l, t)   #iterable datatypes
print(s)


s = {10 ,20, 30}
s.add(100)              #Non iterable datatypes
print(s)
