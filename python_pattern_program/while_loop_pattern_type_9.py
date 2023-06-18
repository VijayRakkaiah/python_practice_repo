row = 5

while row >=1:
    column_1 = 1
    while column_1<=row:
        print(' ', end = " ")
        column_1+=1
        
    column_3 = 5
    value = (65)
    while column_3 >=row:
        print(chr(value), end = " ")
        column_3 -= 1
        value+=1

    column_5 = 5
    value_2 = 65
    while column_5 >= row:
        print(chr(value_2), end =" ")
        column_5-=1
        value_2+=1
        
    print()
    row-=1

row_2 = 1

while row_2 <=5:
    column_2 = 1
    while column_2<=row_2:
        print(' ', end = " ")
        column_2+=1
        
    column_4 = 5
    value_3 = 65
    while column_4 >=row_2:
        print(chr(value_3), end = " ")
        column_4-=1
        value_3+=1

    column_6 = 5
    value_4 = 65
    while column_6 >=row_2:
        print(chr(value_4), end = " ")
        column_6-=1
        value_4+=1
    
    print()
    row_2+=1




##OUTPUT
##
##          A A 
##        A B A B 
##      A B C A B C 
##    A B C D A B C D 
##  A B C D E A B C D E 
##  A B C D E A B C D E 
##    A B C D A B C D 
##      A B C A B C 
##        A B A B 
##          A A 

