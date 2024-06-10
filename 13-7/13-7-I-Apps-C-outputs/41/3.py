
def solve(grid):
    # Check if the grid is valid
    if not is_valid_grid(grid):
        return "SURGERY FAILED"
    
    # Initialize the organs dictionary
    organs = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "E":
                organs[grid[i][j]] = (i, j)
    
    # Initialize the empty space coordinates
    empty_space = (0, 0)
    
    # Initialize the moves list
    moves = []
    
    # Loop until all organs are in their correct positions
    while len(organs) > 0:
        # Get the current organ
        current_organ = list(organs.keys())[0]
        
        # Get the current organ's coordinates
        current_coordinates = organs[current_organ]
        
        # Get the empty space coordinates
        empty_coordinates = empty_space
        
        # Check if the empty space is on the left or right of the current organ
        if current_coordinates[1] == empty_coordinates[1]:
            # Check if the empty space is above or below the current organ
            if current_coordinates[0] > empty_coordinates[0]:
                # Move the organ up
                moves.append("u")
                empty_space = (empty_coordinates[0] + 1, empty_coordinates[1])
            else:
                # Move the organ down
                moves.append("d")
                empty_space = (empty_coordinates[0] - 1, empty_coordinates[1])
        else:
            # Check if the empty space is to the left or right of the current organ
            if current_coordinates[1] > empty_coordinates[1]:
                # Move the organ to the left
                moves.append("l")
                empty_space = (empty_coordinates[0], empty_coordinates[1] + 1)
            else:
                # Move the organ to the right
                moves.append("r")
                empty_space = (empty_coordinates[0], empty_coordinates[1] - 1)
        
        # Update the organs dictionary
        organs[current_organ] = empty_space
        del organs[current_organ]
    
    # Return the moves
    return "SURGERY COMPLETE\n" + "".join(moves)

def is_valid_grid(grid):
    # Check if the grid is valid
    if len(grid) == 0 or len(grid[0]) == 0:
        return False
    
    # Check if the grid is a square
    if len(grid) != len(grid[0]):
        return False
    
    # Check if the grid has an empty space
    if "E" not in grid:
        return False
    
    # Check if the grid has the correct number of organs
    if len(grid) * len(grid[0]) != 4 * len(grid) + 1:
        return False
    
    # Check if the organs are in the correct positions
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "E" and (i, j) not in organs:
                return False
    
    # The grid is valid
    return True

if __name__ == '__main__':
    grid = [[1, 2, 3, 5, 6, "E", 7], [8, 9, 10, 4, 11, 12, 13]]
    print(solve(grid))

