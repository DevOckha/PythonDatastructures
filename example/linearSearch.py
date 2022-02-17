def linear_search(list, item):
    index = 0
    found = False
    
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index += 1
    
    return found


list1 = [12,31,11,55,66,43,76,88,74]

print(linear_search(list1, 88))
print(linear_search(list1, 881))
