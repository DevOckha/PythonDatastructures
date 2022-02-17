"""Giriş listesini iki eşit parçaya böler Her listenin uzunluğu 1 olana kadar bölmek için özyinelemeyi kullanır. Ardından, sıralanan parçaları sıralanmış bir listede birleştirir ve geri döndürür."""


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        a = 0
        b = 0
        c = 0
        
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b+1
            c = c + 1
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1
        
        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list

list1 = [44,13,23,54,66,87,6,4]
merge_sort(list1)
print(list1)