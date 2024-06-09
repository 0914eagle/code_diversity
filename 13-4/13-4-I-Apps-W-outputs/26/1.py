
def get_happy_time(n, x, y, c):
    # Initialize a 2D array to store the state of the table
    table = [[0] * n for _ in range(n)]
    # Set the initial cell as on
    table[x - 1][y - 1] = 1
    # Initialize a variable to store the number of on cells
    on_cells = 1
    # Initialize a variable to store the number of seconds
    seconds = 0
    # Loop until the number of on cells is greater than or equal to c
    while on_cells < c:
        # Loop through each row of the table
        for i in range(n):
            # Loop through each column of the table
            for j in range(n):
                # Check if the current cell is off and has at least one on side-adjacent cell
                if table[i][j] == 0 and sum(table[i - 1][j], table[i + 1][j], table[i][j - 1], table[i][j + 1]) >= 1:
                    # Turn the current cell on
                    table[i][j] = 1
                    # Increment the number of on cells
                    on_cells += 1
        # Increment the number of seconds
        seconds += 1
    # Return the number of seconds
    return seconds

