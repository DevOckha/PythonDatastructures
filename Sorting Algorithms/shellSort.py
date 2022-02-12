def shell_sort(alist):
    gap = len(alist) // 2
    
    while gap > 0:
        for index in range(gap, len(alist)):
            current_element = alist[index]
            pos = index
            
            while pos >= gap and current_element < alist[pos - gap]:
                alist[pos] = alist[pos - gap]
                pos = pos - gap
            
            alist[pos] = current_element
        
        gap = gap // 2
        

num = int(input("list length: "))

alist = [int(input()) for i in range(num)]

shell_sort(alist)

print(alist)