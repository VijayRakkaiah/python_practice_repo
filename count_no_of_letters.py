#dictionary

name= input("Enter name: ")
d = {}
for x in name:
  value = d.get(x, 0)+1
  #print(d)
  d[x] = value
print(d)

#Output:
#Enter name: rajarajachozhan
#{'r': 2, 'a': 5, 'j': 2, 'c': 1, 'h': 2, 'o': 1, 'z': 1, 'n': 1}
