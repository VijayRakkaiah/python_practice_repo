l = [10, 20, 50, 75, 95, 96, 97, 98]
search = int(input("Enter the key to search: "))
min_index = 0
max_index = len(l) - 1

while min_index <= max_index:
    avg_index = (min_index + max_index) // 2
    if search == l[avg_index]:
        print(search, "is available at position", (avg_index + 1))
        break
    elif search > l[avg_index]:
        min_index = avg_index + 1
    else:
        max_index = avg_index - 1
else:
    print("Number not available")
