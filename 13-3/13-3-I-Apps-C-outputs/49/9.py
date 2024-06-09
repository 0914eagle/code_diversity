
def solve_magic_checkerboard(n, m, board):
    # Initialize the minimum sum to a large value
    min_sum = 2001 * 2001
    # Loop through all possible values for the 0 cells
    for i in range(1, 2001):
        for j in range(1, 2001):
            # Check if the current value is valid for the current cell
            if is_valid_value(i, j, n, m, board):
                # Calculate the sum of all values in the board
                sum = calculate_sum(n, m, board)
                # Update the minimum sum if the current sum is smaller
                if sum < min_sum:
                    min_sum = sum
    # Return the minimum sum
    return min_sum

# Check if a value is valid for a cell
def is_valid_value(i, j, n, m, board):
    # Check if the value is already used in the same row
    for k in range(m):
        if board[i][k] == i and k != j:
            return False
    # Check if the value is already used in the same column
    for k in range(n):
        if board[k][j] == i and k != i:
            return False
    # Check if the value is already used in the same diagonal
    for k in range(min(n, m)):
        if board[k][k] == i and i != j:
            return False
    # Check if the value is already used in the opposite diagonal
    for k in range(min(n, m)):
        if board[k][m-k-1] == i and i != j:
            return False
    # Check if the parity of the value is different from the parity of the adjacent cells
    if i % 2 == 0:
        for k in range(m):
            if board[i][k] % 2 == 1 and k != j:
                return False
    else:
        for k in range(m):
            if board[i][k] % 2 == 0 and k != j:
                return False
    return True

# Calculate the sum of all values in the board
def calculate_sum(n, m, board):
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += board[i][j]
    return sum

