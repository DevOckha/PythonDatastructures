def bubleSort(list):
    lastElementIndex = len(list) - 1
    
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    
    return list



list1 = [2,5,4,7,88,66,54]

bubleSort(list1)
print(list1)

"""İki döngü seviyesi nedeniyle, en kötü durum çalışma zamanı karmaşıklığı O(n2) olacaktır."""