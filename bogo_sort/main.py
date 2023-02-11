import random


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        attempts += 1
        random.shuffle(values)
    print(f'Bogo sort attempts: {attempts}')
    return values


# Reading numbers from the file
with open("numbers.txt", "r") as file:
    numbers = [int(number.strip()) for number in file.readlines()]

print(bogo_sort(numbers))

