
def get_min_operations(n, m, table):
    # Initialize the number of operations to 0
    operations = 0
    
    # Loop through each row of the table
    for i in range(n):
        # Loop through each column of the current row
        for j in range(m):
            # If the current cell is good and not a corner, color it
            if table[i][j] == 1 and (i != 1 or j != 1) and (i != n or j != m):
                operations += 1
    
    # Return the minimum number of operations needed to color all good cells
    return operations

