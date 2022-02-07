list1 = [10, 15, 4, 23, 0]

print("unsorted list: ", list1)

for j in range(len(list1)-1, 0, -1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            print(list1)
        else:
            print(list1)
    print()