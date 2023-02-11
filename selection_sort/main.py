import random
from datetime import datetime


def execution_time(function):
    def wrapper(*args, **kwargs):
        before = datetime.now()
        result = function(*args, **kwargs)
        after = datetime.now()
        print(f'Execution time of {function.__name__}(): {(after - before).total_seconds()} s')
        return result
    return wrapper


def get_sample_list(size: int) -> list:
    values = []
    for _ in range(size):
        values.append(random.randint(1, 100))

    return values


def index_of_min(values: list) -> int:
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


@execution_time
def selection_sort(values: list) -> list:
    """
    Sorts given values list using selection sort algorithm.
    :param values: List of values to sort.
    :return: Sorted list.
    """

    sorted_list = []

    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list


numbers = get_sample_list(10000)
# print(numbers)
sorted_numbers = selection_sort(numbers)
# print(sorted_numbers)
