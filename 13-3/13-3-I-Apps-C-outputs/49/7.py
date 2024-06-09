
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

# Check if the current combination forms a valid Magic Checkerboard
def is_valid_magic_checkerboard(n, m, board, i, j):
    # Loop through each row of the checkerboard
    for row in range(n):
        # Check if the numbers in the current row are in strictly increasing order
        if not is_strictly_increasing(board[row]):
            return False
        # Check if the numbers in the current row and the current column are of different parity
        if row == 0:
            if board[row][0] % 2 == i % 2:
                return False
        else:
            if board[row][0] % 2 == board[row - 1][0] % 2:
                return False
    # Loop through each column of the checkerboard
    for col in range(m):
        # Check if the numbers in the current column are in strictly increasing order
        if not is_strictly_increasing([row[col] for row in board]):
            return False
        # Check if the numbers in the current column and the current row are of different parity
        if col == 0:
            if board[0][col] % 2 == j % 2:
                return False
        else:
            if board[0][col] % 2 == board[0][col - 1] % 2:
                return False
    return True

# Check if the numbers in the list are in strictly increasing order
def is_strictly_increasing(my_list):
    for i in range(len(my_list) - 1):
        if my_list[i] >= my_list[i + 1]:
            return False
    return True

# Calculate the sum of all numbers on the checkerboard
def calculate_sum(n, m, board):
    sum = 0
    for row in board:
        for num in row:
            sum += num
    return sum

