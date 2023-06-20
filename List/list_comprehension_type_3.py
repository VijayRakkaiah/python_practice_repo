list_1 = [10, 20, 30, 40, 50]
list_2 = [30, 40, 50, 60, 70]

list_3 = [i for i in list_1 if i not in list_2]

print(list_3)

"""

#Regular method

list_3 = []
for i in list_1:
    if i not in list_2:
        list_3.append(i)
print(list_3)

"""
