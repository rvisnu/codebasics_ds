def InsertionSort(list1):
    for index in range(1, len(list1)):
        current = list1[index]
        posi = index
        while posi-1>=0 and current < list1[posi-1]:
            list1[posi] = list1[posi-1]
            posi-=1
        list1[posi] = current

list1 = [1,3,1,5,7]
print(list1)
InsertionSort(list1)
print(list1)
