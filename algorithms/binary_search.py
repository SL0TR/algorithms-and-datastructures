def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1

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
result = binary_search(numbers, int(target))
verify(result)


