list1 = [34,5,6,81,0,5]

print(f"Unsorted list {list1} ")

for i in range(len(list1)-1):
    min_val = min(list1[1:])
    min_ind = list1.index(min_val)

    if list1[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind], list1[i]

    print(list1)