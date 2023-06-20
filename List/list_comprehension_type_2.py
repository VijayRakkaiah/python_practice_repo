list_1 = [(i*i) for i in range(1,6)]
print(list_1)

list_2 = [value for value in list_1 if value%2==0]
print(list_2)


'''

# reqular method

list_2 = []
for value in list_1:
    if value%2==0:
        list_2.append(value)
print(list_2)

'''
