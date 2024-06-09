
def frequency_sorter(numbers, max_value):
    frequency = [0] * (max_value + 1)
    for number in numbers:
        frequency[number] += 1

    sorted_numbers = sorted(numbers, key=lambda x: (-frequency[x], x))
    return sorted_numbers

