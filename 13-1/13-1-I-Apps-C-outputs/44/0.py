
def n_queens_problem(n, m, board):
    # Initialize variables
    max_queens = 0
    num_ways = 0

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # Check if the current cell is broken
            if board[i][j] == '#':
                continue

            # Check if the current cell is safe for a queen
            safe = True
            for k in range(n):
                # Check if the current cell is in the same row, column, or diagonal as any other queen
                if board[i][k] == 'Q' or board[k][j] == 'Q' or (i - k) == abs(j - k):
                    safe = False
                    break

            # If the current cell is safe for a queen, place a queen on it and update the variables
            if safe:
                board[i][j] = 'Q'
                max_queens += 1
                num_ways += 1

                # Recursively call the function to place the remaining queens
                n_queens_problem(n, m, board)

                # Backtrack and remove the queen from the current cell
                board[i][j] = '.'
                max_queens -= 1

    return max_queens, num_ways

