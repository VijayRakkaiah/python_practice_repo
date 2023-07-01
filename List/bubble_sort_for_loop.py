l = [10, 8, 5, 3, 1, 15, 7]

print('Before sorting:', l)

length = len(l)-1
for j in range (0, length):
  for i in range (0,length):
    if l[i] > l[i+1]:
      l[i], l[i+1] = l[i+1], l[i]
  length-=1
  
print('After sorting:', l)

#Output
#Before sorting: [10, 8, 5, 3, 1, 15, 7]
#After sorting: [1, 3, 5, 7, 8, 10, 15]
