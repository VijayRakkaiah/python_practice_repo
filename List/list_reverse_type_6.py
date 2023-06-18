user_input = input('Enter any sentence: ')

NewList = user_input.split()
i = 0
ReversedList = []

while i<len(NewList):
    if i%2==0:
        ReversedList.append(NewList[i][::-1])
    else:
        ReversedList.append(NewList[i])
    i+=1
    
#print(ReversedList)    #LIST

output = ' '.join(ReversedList)    
print(output)

#INPUT: my name is vijay
#OUTPUT: ['ym', 'name', 'si', 'vijay']  #LIST
#        ym name si vijay
