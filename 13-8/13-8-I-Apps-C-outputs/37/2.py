
def solve(y, x, x_init, map):
    # Initialize the number of paths to 0
    paths = 0

    # Loop through each row of the map
    for i in range(y):
        # Loop through each column of the current row
        for j in range(x):
            # If the current tile is '@', increase the number of paths by 1
            if map[i][j] == '@':
                paths += 1

    # Return the number of paths modulo 1000003
    return paths % 1000003

