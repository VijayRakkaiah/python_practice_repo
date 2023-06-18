user_input = input('Enter any sentence: ')
NewList = user_input.split()
i = 0
ReversedList = []
while i<len(NewList):
    ReversedList.append(NewList[i][::-1])
    i+=2
print(ReversedList)


#INPUT: wish you a very happy new year
#OUTPUT: ['hsiw', 'a', 'yppah', 'raey']
