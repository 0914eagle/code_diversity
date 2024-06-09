
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
                # Check if the cell has a different parity than its neighboring cells
                if (board[row][col] % 2) != (board[row+1][col] % 2) or (board[row][col] % 2) != (board[row][col+1] % 2):
                    return False
            # Check if the current cell is a cell with a number
            if board[row][col] != 0:
                # Check if the current cell is in the top row
                if row == 0:
                    # Check if the current cell has a number that is greater than or equal to the number in the cell below it
                    if board[row][col] >= board[row+1][col]:
                        return False
                # Check if the current cell is in the bottom row
                if row == n-1:
                    # Check if the current cell has a number that is less than or equal to the number in the cell above it
                    if board[row][col] <= board[row-1][col]:
                        return False
                # Check if the current cell is in the left column
                if col == 0:
                    # Check if the current cell has a number that is greater than or equal to the number in the cell to the right of it
                    if board[row][col] >= board[row][col+1]:
                        return False
                # Check if the current cell is in the right column
                if col == m-1:
                    # Check if the current cell has a number that is less than or equal to the number in the cell to the left of it
                    if board[row][col] <= board[row][col-1]:
                        return False
    return True

# Calculate the sum of all numbers on the checkerboard
def calculate_sum(n, m, board):
    sum = 0
    for row in range(n):
        for col in range(m):
            sum += board[row][col]
    return sum

