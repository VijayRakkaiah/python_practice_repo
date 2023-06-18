word = input('Enter any word with number:')
word = word.upper()

#print(word)

for i in  word:
    if i.isdigit():
        i = int(i)
        i = i+64
        print(chr(i), end="")
    else:
        print(i, end='')
