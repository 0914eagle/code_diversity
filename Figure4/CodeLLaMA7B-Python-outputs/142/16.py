def sum_squares(lst):
    
    # Initialize the sum to 0
    sum = 0
    # For each entry in the list
    for i in range(len(lst)):
        # If the index is a multiple of 3
        if i % 3 == 0:
            # Square the entry
            lst[i] = lst[i] ** 2
        # If the index is a multiple of 4 and not a multiple of 3
        elif i % 4 == 0:
            # Cube the entry
            lst[i] = lst[i] ** 3
        # Add the entry to the sum
        sum += lst[i]
    # Return the sum
    return sum


# Define a main() function that prints the results of sum_squares()
