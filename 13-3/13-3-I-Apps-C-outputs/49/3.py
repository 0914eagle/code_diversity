
def solve_magic_checkerboard(n, m, board):
    # Initialize the minimum sum to a large value
    min_sum = 10000
    # Loop through all possible combinations of numbers for the 0 cells
    for i in range(1, 2001):
        for j in range(1, 2001):
            # Check if the current combination forms a valid Magic Checkerboard
            if is_valid_magic_checkerboard(n, m, board, i, j):
                # Calculate the sum of all numbers on the checkerboard
                sum = calculate_sum(n, m, board)
                # Update the minimum sum if the current sum is smaller
                if sum < min_sum:
                    min_sum = sum
    # Return the minimum sum
    return min_sum

# Check if a Magic Checkerboard is valid
def is_valid_magic_checkerboard(n, m, board, i, j):
    # Check if the current combination forms a valid Magic Checkerboard
    for row in range(n):
        for col in range(m):
            # Check if the current cell is a corner cell
            if (row == 0 or row == n-1) and (col == 0 or col == m-1):
                # Check if the numbers in the corner cells have different parity
                if (board[row][col] + board[row+1][col+1]) % 2 == 0:
                    return False
            # Check if the current cell is a non-corner cell
            elif (row > 0 and row < n-1) and (col > 0 and col < m-1):
                # Check if the numbers in the non-corner cells are in increasing order
                if board[row][col] >= board[row-1][col] and board[row][col] >= board[row+1][col] and board[row][col] >= board[row][col-1] and board[row][col] >= board[row][col+1]:
                    return False
    # If the current combination forms a valid Magic Checkerboard, return True
    return True

# Calculate the sum of all numbers on the checkerboard
def calculate_sum(n, m, board):
    sum = 0
    for row in range(n):
        for col in range(m):
            sum += board[row][col]
    return sum

