user_input = input('Enter any sentence: ')
NewList = user_input.split()
i = len(NewList)-1
ReversedList = []
while i>=0:
    ReversedList.append(NewList[i])
    i-=1
print(ReversedList)
