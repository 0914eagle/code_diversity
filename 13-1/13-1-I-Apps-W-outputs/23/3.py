
def get_max_even_coins(grid):
    # Initialize the number of even coins to 0
    num_even_coins = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # Check if the current cell contains an even number of coins
            if grid[i][j] % 2 == 0:
                # Increment the number of even coins
                num_even_coins += 1
    
    # Return the number of even coins
    return num_even_coins

