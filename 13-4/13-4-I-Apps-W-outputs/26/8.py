
def get_happy_seconds(n, x, y, c):
    # Initialize a 2D array to represent the table
    table = [[0] * n for _ in range(n)]
    # Set the initial cell as switched on
    table[x - 1][y - 1] = 1
    # Initialize a variable to keep track of the number of switched on cells
    switched_on = 1
    # Initialize a variable to keep track of the number of seconds
    seconds = 0
    # Loop until the number of switched on cells is greater than or equal to c
    while switched_on < c:
        # Loop through each row of the table
        for i in range(n):
            # Loop through each column of the table
            for j in range(n):
                # If the current cell is switched off and has at least one switched on side-adjacent cell
                if table[i][j] == 0 and sum(table[i - 1][j], table[i + 1][j], table[i][j - 1], table[i][j + 1]) >= 1:
                    # Switch on the current cell
                    table[i][j] = 1
                    # Increment the number of switched on cells
                    switched_on += 1
        # Increment the number of seconds
        seconds += 1
    # Return the number of seconds
    return seconds

