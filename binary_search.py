numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]

def find(number_list, end, number_to_check, start=0, pointer=0):
    reference = number_list[pointer]
    
    if start >  end:
        return -1
    
    if number_list[pointer] == number_to_check:
        return pointer
    
    if number_to_check < reference:
        end = pointer
        pointer = (start + end) // 2
    else:
        start = pointer
        pointer = (start + end) // 2
    
    return find(number_list, end, number_to_check, start, pointer)
    
def find_all(number_list, number_to_check):
    list_of_index = []
    index = find(numbers, len(numbers), number_to_check, 0, len(numbers)//2 )
    list_of_index.append(index)
    
    # finding_left
    i = index - 1
    while i > 0:
        if number_list[i] == number_to_check:
            list_of_index.append(i)
        else:
            break
        i = i - 1

    # finding_right
    i = index + 1
    while i < len(number_list):
        if number_list[i] == number_to_check:
            list_of_index.append(i)
        else:
            break
        i = i + 1 
    print(list_of_index)

print(find(numbers, len(numbers), 4, 0, len(numbers)//2 ))
find_all(numbers,15)
