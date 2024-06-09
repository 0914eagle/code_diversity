
def renumber_items(n, current_numbers):
    # Create a dictionary to map the current numbers to their indices
    current_number_to_index = {current_number: index for index, current_number in enumerate(current_numbers)}
    
    # Initialize the new numbers to be the same as the current numbers
    new_numbers = list(current_numbers)
    
    # Loop through the current numbers and find any duplicates
    for current_number in current_numbers:
        # If the current number is not unique, replace it with the next available number
        if current_numbers.count(current_number) > 1:
            # Find the index of the current number in the current number to index dictionary
            index = current_number_to_index[current_number]
            
            # Replace the current number with the next available number
            new_numbers[index] = index + 1
    
    return new_numbers

