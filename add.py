word = 'ABCdEfg'

for i in range(len(word)):
    if word[i]>='A' and word[i]<='Z':
        print(chr(ord(word[i])+32), end='')

    else:
        print(word[i], end = '')