l = [10, 8, 5, 3, 1, 15]

print('Before sorting:', l)
print("hello")
j = 1
while j < len(l):
  i = 0
  while i < len(l) - 1:
    if l[i] > l[i + 1]:
      l[i], l[i + 1] = l[i + 1], l[i]
    i += 1
  j += 1
  
print('After sorting:', l)

#Output:
#Before sorting: [10, 8, 5, 3, 1, 15]
#After sorting: [1, 3, 5, 8, 10, 15]
