def insertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        element_next = list[i]
    
        while (list[i] > element_next) and (j >= 0):
            list[j+1] = list[j]
            j -= 1
        list[j+1] = element_next
    return list


list1 =[33,44,54,66,57,99,76]

print(insertionSort(list1))