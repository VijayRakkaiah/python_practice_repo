user_input = input('Enter any sentence: ')
NewList = user_input.split()
i = 0
ReversedList = []
while i<len(NewList):
    ReversedList.append(NewList[i])
    i+=2
print(ReversedList)
