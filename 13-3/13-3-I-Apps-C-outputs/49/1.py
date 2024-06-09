
def solve_magic_checkerboard(n, m, board):
    # Initialize the minimum sum to a large value
    min_sum = 10000
    # Loop through all possible values for the 0 cells
    for i in range(1, 2001):
        for j in range(1, 2001):
            # Check if the current value is valid for the Magic Checkerboard
            if is_valid_magic_checkerboard(n, m, board, i, j):
                # Calculate the sum of all values in the board
                sum = calculate_sum(n, m, board)
                # Update the minimum sum if the current sum is smaller
                if sum < min_sum:
                    min_sum = sum
    # Return the minimum sum
    return min_sum

def is_valid_magic_checkerboard(n, m, board, i, j):
    # Check if the current value is valid for the Magic Checkerboard
    for row in range(n):
        for col in range(m):
            if board[row][col] == 0:
                board[row][col] = i
            if board[row][col] == i and board[row][col-1] == j:
                return False
    return True

def calculate_sum(n, m, board):
    # Calculate the sum of all values in the board
    sum = 0
    for row in range(n):
        for col in range(m):
            sum += board[row][col]
    return sum

