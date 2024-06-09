
def renumber_items(n, initial_numbers):
    # Sort the initial numbers in ascending order
    sorted_numbers = sorted(initial_numbers)
    # Create a dictionary to map the initial numbers to their indices in the sorted list
    number_to_index = {number: index for index, number in enumerate(sorted_numbers)}
    # Create a list to store the final numbers
    final_numbers = [0] * n
    # Fill the list with the final numbers in the order of the initial numbers
    for i in range(n):
        final_numbers[i] = number_to_index[initial_numbers[i]] + 1
    return final_numbers

