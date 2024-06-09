
def solve(y, x, x_init, map):
    # Initialize the number of paths to 0
    num_paths = 0
    
    # Loop through each row of the map
    for y in range(y):
        # Loop through each column of the map
        for x in range(x):
            # If the current tile is the castle, increment the number of paths
            if map[y][x] == '@':
                num_paths += 1
    
    # Return the number of paths modulo 1000003
    return num_paths % 1000003

