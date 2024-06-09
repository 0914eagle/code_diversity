
def n_queens_problem(n, m, board):
    # Initialize a list to store the positions of the queens
    queens = []
    # Initialize a variable to store the number of ways to place the queens
    ways = 0

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # If the current cell is not broken and has not been visited yet
            if board[i][j] == "." and (i, j) not in queens:
                # Add the current cell to the list of queens
                queens.append((i, j))
                # Recursively call the function to place the remaining queens
                ways += n_queens_problem(n, m, board, queens)
                # Remove the current cell from the list of queens
                queens.pop()

    # If there are no more cells to place queens on, return the number of ways to place the queens
    if len(queens) == n:
        return ways

    # If there are still cells to place queens on, recursively call the function to place the remaining queens
    return n_queens_problem(n, m, board, queens)

