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


def recursive_binary_search(values, target):
    """Returns Ture if target exist, other way False"""
    if len(values) == 0:
        return False
    else:
        midpoint = len(values) // 2

        if values[midpoint] == target:
            return True
        else:
            if values[midpoint] < target:
                return recursive_binary_search(values[midpoint+1:], target)
            else:
                return recursive_binary_search(values[:midpoint], target)


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list.")


def verify_recursive(result):
    print("Target found:", result)


# Sorted list of numbers
numbers = [num for num in range(1, 101)]

# result = binary_search(numbers, 100)
# verify(result)

result = recursive_binary_search(numbers, 100)
verify_recursive(result)
