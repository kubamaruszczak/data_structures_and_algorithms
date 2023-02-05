def linear_search(values, target):
    """
    Return the index position of the target if found, else returns None
    """

    for idx in range(len(values)):
        if values[idx] == target:
            return idx
    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list.")


numbers = [num for num in range(1, 11)]

result = linear_search(numbers, 11)
verify(result)

result = linear_search(numbers, 6)
verify(result)
