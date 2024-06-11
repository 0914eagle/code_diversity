def sum_squares(lst):
    
    # Initialize the sum variable
    sum = 0
    
    # Iterate through the list
    for i in range(len(lst)):
        # Check if the index is a multiple of 3
        if i % 3 == 0:
            # If it is, square the value
            sum += lst[i] ** 2
        # Check if the index is a multiple of 4
        elif i % 4 == 0:
            # If it is, cube the value
            sum += lst[i] ** 3
        # If it is not a multiple of 3 or 4, add the value to the sum
        else:
            sum += lst[i]
    # Return the sum
    return sum


# Tests
