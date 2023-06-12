age = int(input("Please enter your age: "))

if age > 5:
    
    nationality = input ("Please enter your nationality: ")
    nationality_2 = nationality.lower()

    if nationality_2 == 'indian':
        print("Eligible for aadhar card")
    else:
        print("Not for other nationalities")
        
else:
    print("Age criteria not met")
