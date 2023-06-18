word = input ("Enter any word: ")

number = 0
length = len(word)
count = 0

while number < length:
    
    if word[number] in ['a', 'e', 'i', 'o', 'u'] or word[number] in ['A', 'E', 'I', 'O', 'U']:
        print(word[number], end = ' ')
        count+=1
        
    number = number + 1

print()    
print('vowels count is:',count)
