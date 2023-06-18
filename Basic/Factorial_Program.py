first_number = 1
factorial_number = int(input("Enter any number: "))
total = 1

while first_number <= factorial_number:
    total = total * first_number
    first_number+=1
    
print("Factorial of",factorial_number,"is: ",total)
