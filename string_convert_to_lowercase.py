Input = 'LOWER case UppER CAse'
    
for i in range(len(Input)):
    if Input[i]>='A' and Input[i]<='Z':
        print(chr(ord(Input[i])+32), end='')

    else:
        print(Input[i], end = '')
