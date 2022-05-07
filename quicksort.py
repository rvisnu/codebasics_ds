def pivot_in_place(elements, start, end):
    pivot = start
    left = start+1
    right = end

    while True:
        while left<=right and elements[left] <= elements[pivot]:
            left += 1
        while left<=right and elements[right] > elements[pivot]:
            right -= 1

        if left > right:
            break
        else:
            elements[right], elements[left] = elements[left], elements[right]
    elements[pivot], elements[right] = elements[right], elements[pivot]
    return right


def quicksort(elements, start, end):
    if start<end:
        p = pivot_in_place(elements, start, end)
        quicksort(elements, start, p-1)
        quicksort(elements, p+1, end)


if __name__ == "__main__":
    number = [[16, 2, 15, 43, 25, 1, 4], [1,100], [3], ["a","d","s","f","h","a"]]
    for numbers in number:
        print(numbers)
        quicksort(numbers, 0,len(numbers)-1)
        print(numbers)
