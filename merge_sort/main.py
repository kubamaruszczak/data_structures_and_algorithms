def merge_sort(values: list):
    """
    Sort a list in ascending order.
    Returns a new sorted list.

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublist created in previous steps

    Takes O(n log n) time.
    """

    # Base case - stopping condition
    if len(values) <= 1:
        return values

    left_half, right_half = split(values)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(values: list):
    """
    Divide the unsorted list at midpoint into sublist.
    Returns two sublists - left and right

    Takes overall O(log n) time.
    """

    midpoint = len(values) // 2
    left = values[:midpoint]
    right = values[midpoint:]

    return left, right


def merge(left: list, right: list):
    """
    Merges two lists, sorting them in the process.
    Returns a new merged list

    Runs in overall O(n) time.
    """

    new_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    while i < len(left):
        new_list.append(left[i])
        i += 1

    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list


def verify_sorted(values: list):
    n = len(values)

    if n == 0 or n == 1:
        return True

    return values[0] <= values[1] and verify_sorted(values[1:])


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 77]
sorted_list = merge_sort(a_list)
print(verify_sorted(a_list))
print(verify_sorted(sorted_list))
