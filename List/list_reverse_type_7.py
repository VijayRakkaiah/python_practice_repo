input = 'sun mon tues wednes thurs fri satur'
words = input.split()
word_2 = []
for word in words:
    word_2.append(word + 'day')

output = ', '.join(word_2)
print(output)


#OUTPUT: sunday, monday, tuesday, wednesday, thursday, friday, saturday
