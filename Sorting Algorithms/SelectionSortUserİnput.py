num = int(input("how many numbers you want to enter?: "))


list1 = [int(input("enter number: ")) for x in range(num)]
print(f"unsorted list {list1}")

for i in range(len(list1) - 1):
    m_val = list1[i]

    for j in range(i+1, len(list1)):
        if list1[j] > m_val:
            m_val = list1[j]
    

    m_ind = list1.index(m_val, i)

    if list1[i] != list1[m_ind]:
        list1[i], list1[m_ind] = list1[m_ind], list1[i]


print(list1)