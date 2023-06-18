row = 1

while row <= 5:
    column_1 =1
    while column_1 < row:
        print(' ', end = " ")
        column_1+=1
    column_2 = 5
    while column_2>=row:
        print(row, end = ' ')
        column_2-=1    
    print()
    row+=1

##OUTPUT
    
##1 1 1 1 1 
##  2 2 2 2 
##    3 3 3 
##      4 4 
##        5 
