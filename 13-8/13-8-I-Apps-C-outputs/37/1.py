
def count_paths(map):
    # Initialize the number of paths to 0
    paths = 0
    
    # Loop through each row of the map
    for row in map:
        # Loop through each column of the current row
        for col in row:
            # If the current cell is '@', increase the number of paths by 1
            if col == '@':
                paths += 1
    
    # Return the number of paths
    return paths

