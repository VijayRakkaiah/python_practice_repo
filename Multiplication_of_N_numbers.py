first_number = int(input("Enter First Number: "))
last_number = int(input("Enter Last number: "))
total = 1

while first_number <= last_number:
    total = total * first_number
    first_number+=1
    
print('The multiplication of given number is:',total)
