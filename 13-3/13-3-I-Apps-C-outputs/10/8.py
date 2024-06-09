
def n_queens_problem(n, m, board):
    # Initialize variables
    queens = []
    max_queens = 0
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
                max_queens, ways = n_queens_problem(n, m, board, queens)
                # If the current queen placement is valid, update the maximum number of queens and ways
                if max_queens > 0:
                    max_queens += 1
                    ways += 1
                # Remove the current queen from the list of queens
                queens.pop()

    # Return the maximum number of queens and ways
    return max_queens, ways

def n_queens_problem_extended(n, m, board):
    # Initialize variables
    queens = []
    max_queens = 0
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
                max_queens, ways = n_queens_problem_extended(n, m, board, queens)
                # If the current queen placement is valid, update the maximum number of queens and ways
                if max_queens > 0:
                    max_queens += 1
                    ways += 1
                # Remove the current queen from the list of queens
                queens.pop()

    # Return the maximum number of queens and ways
    return max_queens, ways

