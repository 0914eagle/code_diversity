
def get_happy_seconds(n, x, y, c):
    # Initialize a 2D array to represent the table
    table = [[0] * n for _ in range(n)]
    
    # Set the initial cell to 1
    table[x - 1][y - 1] = 1
    
    # Iterate through each second
    for second in range(1, n * n + 1):
        # Get the number of switched on cells
        num_on_cells = sum(map(sum, table))
        
        # If the number of switched on cells is greater than or equal to c, return the current second
        if num_on_cells >= c:
            return second
        
        # Otherwise, switch on the cells that are off but have the side-adjacent cells that are on
        for i in range(n):
            for j in range(n):
                if table[i][j] == 0 and any(table[i][k] == 1 for k in (j - 1, j, j + 1) if 0 <= k < n):
                    table[i][j] = 1
    
    # If we reach this point, it means that Mr. Bender will never be happy
    return -1

