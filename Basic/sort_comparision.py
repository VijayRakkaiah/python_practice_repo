word_one = input ("Please enter first word: ")
word_two = input ("Please enter second word: ")

if sorted (word_one) == sorted (word_two):
    print("Both are same")

else:
    print("Not same")


#print(sorted (word_one))
#print(sorted (word_two))

#output
#Please enter first word: vijay deiva
#Please enter second word: deiva vijay

#Both are same

#[' ', 'a', 'a', 'd', 'e', 'i', 'i', 'j', 'v', 'v', 'y']
#[' ', 'a', 'a', 'd', 'e', 'i', 'i', 'j', 'v', 'v', 'y']
