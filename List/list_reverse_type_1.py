NewList = ['a', 'b', 'c', 'd']
i = len(NewList)-1
ReversedList = []
while i>=0:
    ReversedList.append(NewList[i])
    i-=1
print(ReversedList)
