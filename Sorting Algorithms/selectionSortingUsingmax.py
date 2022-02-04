list1 = [56,3,2,78,6,0]
print(list1)

for i in range(len(list1)):
    max_value = max(list1[i:])
    max_index = list1.index(max_value)
    list1[i], list1[max_index] = list1[max_index], list1[i]

print(list1)