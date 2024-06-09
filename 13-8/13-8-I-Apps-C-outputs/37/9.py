
def solve(y, x, x_init, map):
    # Initialize the number of possible paths to 0
    num_paths = 0
    
    # Iterate through each row of the map
    for row in range(y):
        # Iterate through each column of the map
        for col in range(x):
            # If the current tile is a '>' or '<' current, check if the ship can move in that direction
            if map[row][col] == '>' or map[row][col] == '<':
                # If the ship can move in the current direction, increment the number of possible paths
                num_paths += 1
    
    # Return the number of possible paths modulo 1000003
    return num_paths % 1000003

