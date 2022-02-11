def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        current_elemt = my_list[index]
        pos = index
        
        while current_elemt < my_list[pos - 1] and pos > 0:
            my_list[pos] = my_list[pos - 1]
            pos = pos - 1
        
        my_list[pos] = current_elemt


list1 = [2,3,4,5,1]
insertion_sort(list1)
print(list1)