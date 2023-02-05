def binary_search(values, target):
    first = 0
    last = len(values) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if values[midpoint] == target:
            return midpoint
        elif values[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list.")


# Sorted list of numbers
numbers = [num for num in range(1, 101)]

result = binary_search(numbers, 100)
verify(result)
