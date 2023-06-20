l = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
     ]

print('Before transposing matrix')
for i in range (len(l)):
    for j in range (len(l[i])):
        print(l[i][j], end = " ")
    print()
print()

print('After transposing matrix')
for i in range (len(l)):
    for j in range (len(l[i])):
        l[i][j]# = l[j][i]
        print(l[i][j], end=' ')
    print()

#OUTPUT

#Before transposing matrix
#10 20 30 
#40 50 60 
#70 80 90 

#After transposing matrix
#10 40 70 
#40 50 80 
#70 80 90
