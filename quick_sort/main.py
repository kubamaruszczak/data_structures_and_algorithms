import random


def get_sample_list(size: int) -> list:
    values = []
    for _ in range(size):
        values.append(random.randint(1, 100))

    return values


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


numbers = get_sample_list(10000)
# print(numbers)
sorted_list = quick_sort(numbers)
# print(sorted_list)
