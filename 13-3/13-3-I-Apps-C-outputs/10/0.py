
def n_queens_problem(n, m, board):
    # Initialize a list to store the positions of the queens
    queens = []
    # Initialize a variable to store the number of ways to place queens
    ways = 0

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # If the current cell is not broken and there is no queen in the current row
            if board[i][j] == "." and i not in queens:
                # Add the current queen to the list of queens
                queens.append(i)
                # Increment the number of ways to place queens
                ways += 1
                # Break out of the inner loop to avoid placing multiple queens in the same row
                break

    # Return the maximum number of queens and the number of ways to place them
    return len(queens), ways

