import pprint

def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    print(numbers)

def bubble_sort_elements(elements, key="name"):
    for i in range(len(elements)-1):
        for j in range(i, len(elements)):
            if elements[i][key] > elements[j][key]:
                elements[i], elements[j] = elements[j], elements[i]
    pprint.pprint(elements)


if __name__ == "__main__":
    numbers = [16, 2, 15, 43, 25, 1]
    bubble_sort(numbers)

    elements = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    bubble_sort_elements(elements)
    bubble_sort_elements(elements, key='device')
    bubble_sort_elements(elements, key='transaction_amount')
