
def renumber_items(numbers):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Create a dictionary to map the original numbers to their new indices
    number_map = {number: index for index, number in enumerate(sorted_numbers, 1)}
    # Return the new numbers in the order they occur in the input
    return [number_map[number] for number in numbers]

