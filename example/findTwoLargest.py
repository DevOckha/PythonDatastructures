def largest_two(list1):
    my_max, second = list1[:2]
    if my_max < second:
        my_max, second = second, my_max
    
    for idx in range(2, len(list1)):
        if my_max < list1[idx]:
            my_max, second = list1[idx], my_max
        
        elif second < list1[idx]:
            second = list1[idx]
    
    return (my_max, second)



my_list = [2,3,44,5,66,76,54,77,89,99]

print(largest_two(my_list))