def InsertionSort(list1):
    output = []
    output.append(list1[0])
    for index in range(1, len(list1)):
        current = list1[index]
        posi = index
        while posi-1>=0 and current < list1[posi-1]:
            list1[posi] = list1[posi-1]
            posi-=1
        list1[posi] = current
        get_median(list1[:index+1], output)
    for i in output: print(i)

def get_median(arr, output):
    if len(arr)%2 == 0:
        m = len(arr) // 2
        n = m - 1
        avg = (arr[m] + arr[n]) / 2
        output.append(avg)
    else:
        m = len(arr) // 2
        output.append(arr[m])

list1 = [2, 1, 5, 7, 2, 0, 5]
#(list1)
InsertionSort(list1)
#print(list1)

