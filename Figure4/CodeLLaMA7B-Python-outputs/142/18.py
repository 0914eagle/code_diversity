def sum_squares(lst):
    
    # Initialize a variable to hold the sum of squares
    sum_squares = 0
    
    # Iterate through the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the value
        if i % 3 == 0:
            sum_squares += lst[i]**2
        # If the index is a multiple of 4, but not a multiple of 3, cube the value
        elif i % 4 == 0:
            sum_squares += lst[i]**3
        # Otherwise, do nothing
        else:
            pass
    # Return the sum of squares
    return sum_squares
