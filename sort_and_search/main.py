import random

from names import names_list


def linear_search(collection, target):
    for i in range(len(collection)):
        if target == collection[i]:
            return i
    return None


def binary_search(collection, target):
    first = 0
    last = len(collection) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def quick_sort(values: list) -> list:
    if len(values) <= 1:
        return values

    pivot = values[0]
    less_than_pivot = []
    grater_than_pivot = []

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            grater_than_pivot.append(value)

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(grater_than_pivot)


# Choose random name to search for
search_for = random.choice(names_list)

# Sort the list of names using quick sort
sorted_names = quick_sort(names_list)

# Search for the name using linear search
index = linear_search(sorted_names, search_for)
print(index)

# Search for the name using binary search
index2 = binary_search(sorted_names, search_for)
print(index)
