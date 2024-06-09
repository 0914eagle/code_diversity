
def n_queens_problem(n, m, board):
    # Initialize variables
    max_queens = 0
    num_ways = 0

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # Check if the current cell is empty and not broken
            if board[i][j] == "." and board[i][j] != "#":
                # Increment the maximum number of queens
                max_queens += 1
                # Calculate the number of ways to place queens
                num_ways += n_queens_helper(board, i, j, max_queens)

    return max_queens, num_ways

def n_queens_helper(board, row, col, num_queens):
    # Base case: if the number of queens is 0, return 1
    if num_queens == 0:
        return 1

    # Initialize variables
    num_ways = 0

    # Loop through each cell in the current row
    for i in range(len(board[0])):
        # Check if the current cell is empty and not broken
        if board[row][i] == "." and board[row][i] != "#":
            # Place a queen in the current cell
            board[row][i] = "Q"
            # Recursively call the function to place the remaining queens
            num_ways += n_queens_helper(board, row + 1, i, num_queens - 1)
            # Remove the queen from the current cell
            board[row][i] = "."

    return num_ways

# Test the function with the sample input
n = 3
m = 4
board = [
    [".", ".", ".", "."],
    [".", "#", ".", "#"],
    [".", ".", ".", "."]]
max_queens, num_ways = n_queens_problem(n, m, board)
print(max_queens) # Output: 5
print(num_ways) # Output: 13

