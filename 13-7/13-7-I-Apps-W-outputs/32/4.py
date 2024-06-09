
def renumber_items(n, initial_numbers):
    numbers = list(set(initial_numbers))
    numbers.sort()
    mapping = {old_number: new_number for old_number, new_number in zip(numbers, range(1, len(numbers) + 1))}
    return [mapping[number] for number in initial_numbers]

