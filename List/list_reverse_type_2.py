User_Input = input('Enter any word: ')
NewList = list(User_Input)
i = len(NewList)-1
ReversedList = []
while i>=0:
    ReversedList.append(NewList[i])
    i-=1
print(ReversedList)
