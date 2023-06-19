l = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
     ]

# solution : 1
for i in range (len(l)):
    for j in range (len(l[i])):
        if i==j:
            print(l[i][j])

#solution : 2
#for i in range (len(l)):
#    print([i][i])
