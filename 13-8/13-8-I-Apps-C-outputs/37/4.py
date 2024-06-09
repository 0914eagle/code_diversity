
def solve(y, x, x_init, map):
    # Initialize the number of paths to 0
    num_paths = 0
    
    # Iterate through each row of the map
    for i in range(y):
        # Iterate through each column of the current row
        for j in range(x):
            # If the current tile is a '>' and the next tile is not a '<' or '#', then we can move east
            if map[i][j] == '>' and map[i][j+1] not in ['<', '#']:
                # Increment the number of paths
                num_paths += 1
            # If the current tile is a '<' and the previous tile is not a '>' or '#', then we can move west
            elif map[i][j] == '<' and map[i][j-1] not in ['>', '#']:
                # Increment the number of paths
                num_paths += 1
    
    # Return the number of paths modulo 1000003
    return num_paths % 1000003

