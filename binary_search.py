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

print(find(numbers, len(numbers), 4, 0, len(numbers)//2 ))
