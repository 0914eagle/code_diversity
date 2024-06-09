
def find_paths(y, x, x_init, map):
    # Initialize the number of paths to 0
    paths = 0
    
    # Loop through each row of the map
    for i in range(y):
        # If the current row is the last row and the current column is the castle column
        if i == y-1 and map[i][x_init] == '@':
            # Increment the number of paths
            paths += 1
        
        # Loop through each column of the current row
        for j in range(x):
            # If the current column is the castle column and the current row is not the last row
            if j == x_init and i < y-1:
                # Increment the number of paths
                paths += 1
            
            # If the current tile is a current tile
            if map[i][j] in ['>', '<']:
                # If the current tile is a current tile and the next tile is not a current tile or a wall
                if map[i][j] == '>' and (j == x-1 or map[i][j+1] not in ['>', '#']):
                    # Increment the number of paths
                    paths += 1
                # If the current tile is a current tile and the previous tile is not a current tile or a wall
                elif map[i][j] == '<' and (j == 0 or map[i][j-1] not in ['<', '#']):
                    # Increment the number of paths
                    paths += 1
    
    # Return the number of paths
    return paths % 1000003

