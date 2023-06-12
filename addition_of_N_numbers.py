first_number = int(input("Enter First Number: "))
last_number = int(input("Enter Last number: "))
total = 0

while first_number <= last_number:
    total = total + first_number
    first_number+=1
    
print('The addition off given number is:',total)
