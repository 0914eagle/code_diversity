
def rate_dance(grid):
    # Initialize variables
    rating = 0
    current_move = 0
    previous_move = 0

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current character is '$'
            if grid[i][j] == '$':
                # Increment the current move
                current_move += 1
            # Check if the current character is '_' and the previous character was '$'
            elif grid[i][j] == '_' and grid[i][j-1] == '$':
                # Increment the rating
                rating += 1
                # Reset the current move
                current_move = 0
            # Check if the current character is '_' and the previous character was '_'
            elif grid[i][j] == '_' and grid[i][j-1] == '_':
                # Increment the previous move
                previous_move += 1

    # Return the rating
    return rating

