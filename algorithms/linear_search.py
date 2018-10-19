def linear_search(list, trgt):
    for i in range(0, len(list)):
        if list[i] == trgt:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


list_length = input("Enter the range of the linear list: ")
numbers = []

for number in range(0, int(list_length)):
    numbers.append(number+1)

target = input("Enter the target: ")
result = linear_search(numbers, int(target))
verify(result)
