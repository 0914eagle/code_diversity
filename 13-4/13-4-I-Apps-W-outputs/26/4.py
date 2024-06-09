
def get_happy_time(n, x, y, c):
    # Initialize a 2D array to represent the table
    table = [[0] * n for _ in range(n)]
    
    # Set the initial cell to 1
    table[x-1][y-1] = 1
    
    # Initialize a variable to keep track of the number of switched on cells
    switched_on = 1
    
    # Iterate until the condition is met
    while switched_on < c:
        # Iterate over the table
        for i in range(n):
            for j in range(n):
                # Check if the cell is off and has at least one on side-adjacent cell
                if table[i][j] == 0 and sum(table[i-1][j], table[i+1][j], table[i][j-1], table[i][j+1]) >= 1:
                    # Switch on the cell
                    table[i][j] = 1
                    switched_on += 1
    
    # Return the number of iterations
    return switched_on

