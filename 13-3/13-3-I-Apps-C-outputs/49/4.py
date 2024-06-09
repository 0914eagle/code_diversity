
def solve_magic_checkerboard(n, m, board):
    # Initialize the minimum sum to a large value
    min_sum = 10000
    # Loop through all possible combinations of numbers for the 0 cells
    for i in range(1, 2001):
        for j in range(1, 2001):
            # Check if the current combination forms a valid Magic Checkerboard
            if is_valid_magic_checkerboard(n, m, board, i, j):
                # Calculate the sum of all numbers on the board
                sum = calculate_sum(n, m, board)
                # Update the minimum sum if the current sum is smaller
                if sum < min_sum:
                    min_sum = sum
    # Return the minimum sum
    return min_sum

# Check if a Magic Checkerboard is valid
def is_valid_magic_checkerboard(n, m, board, i, j):
    # Check if the board is valid
    if not is_valid_board(n, m, board):
        return False
    # Check if the cells that share only a corner have different parity
    for row in range(n):
        for col in range(m):
            if board[row][col] == 0:
                continue
            if row > 0 and col > 0 and board[row][col] == board[row-1][col-1]:
                return False
    return True

# Calculate the sum of all numbers on the board
def calculate_sum(n, m, board):
    sum = 0
    for row in range(n):
        for col in range(m):
            sum += board[row][col]
    return sum

# Check if the board is valid
def is_valid_board(n, m, board):
    # Check if the board is not empty
    if len(board) == 0:
        return False
    # Check if the board has the correct number of rows and columns
    if len(board[0]) != m:
        return False
    # Check if the numbers in each column are in strictly increasing order
    for col in range(m):
        for row in range(n-1):
            if board[row][col] > board[row+1][col]:
                return False
    # Check if the numbers in each row are in strictly increasing order
    for row in range(n):
        for col in range(m-1):
            if board[row][col] > board[row][col+1]:
                return False
    return True

