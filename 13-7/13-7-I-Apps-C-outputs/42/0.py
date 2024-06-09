
def get_max_flowers(field, start_row, start_col):
    # Initialize a list to store the number of petals on each flower
    petals = []
    # Iterate over the field and append the number of petals on each flower to the list
    for row in field:
        for col in row:
            petals.append(col)
    # Initialize a variable to store the maximum number of flowers visited
    max_flowers = 0
    # Initialize a variable to store the current number of flowers visited
    curr_flowers = 0
    # Initialize a variable to store the current row and column indices
    row_idx, col_idx = start_row - 1, start_col - 1
    # Iterate until we have visited all the flowers in the field
    while row_idx < len(field) and col_idx < len(field[0]):
        # Increment the current number of flowers visited
        curr_flowers += 1
        # Get the number of petals on the current flower
        curr_petals = petals[row_idx * len(field[0]) + col_idx]
        # Get the number of petals on the next flower in the same row
        next_petals = petals[row_idx * len(field[0]) + col_idx + 1]
        # If the number of petals on the next flower is greater than the current flower, we can move to the next flower
        if next_petals > curr_petals:
            col_idx += 1
        # Otherwise, we need to move to the next row
        else:
            row_idx += 1
            col_idx = 0
        # Update the maximum number of flowers visited
        max_flowers = max(max_flowers, curr_flowers)
    # Return the maximum number of flowers visited
    return max_flowers

