def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        j = 0
        i = 0
        k = 0
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
                
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1
            while i < len(left_list):
                list1[k] = left_list[i]
                i += 1
                k += 1
            while j < len(right_list):
                list1[k] = right_list[j]
                j += 1
                k += 1


num = int(input("how many elements you want in list: "))
list1 = [int(input()) for x in range(num)]

merge_sort(list1)

print("sorted list is: ", list1)