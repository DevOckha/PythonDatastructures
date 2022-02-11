def largest(list1):
    my_max = list1[0]
    for idx in range(1,len(list1)):
        if my_max < list1[idx]:
            my_max = list1[idx]
    
    return my_max


my_list = [2,3,5,67,88,87,55]
print(largest(my_list))
