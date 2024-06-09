
def n_queens(n, m, board):
    # Initialize variables
    queens = []
    ways = 0

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # If the current cell is not broken and not already occupied by a queen
            if board[i][j] == "." and j not in queens:
                # Add the current cell to the list of queens
                queens.append(j)
                # Recursively call the function to place the next queen
                ways += n_queens(n, m, board, queens)
                # Remove the current queen from the list
                queens.pop()

    # If all queens have been placed, return the number of ways
    if len(queens) == n:
        return ways
    # If not all queens have been placed, return 0
    else:
        return 0

