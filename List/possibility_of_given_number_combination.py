given_list = [1, 2, 3, 4, 5]

length = len(given_list)
new_list = []

for j in range(0,(length)):
  for i in range(0,(length)):
    val = [given_list[j],given_list[i]]
    join_value = ''.join(str(k) for k in val)
    new_join_value = int(join_value)
    new_list.append(new_join_value)
    
print(new_list)

#Output
#[11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]
