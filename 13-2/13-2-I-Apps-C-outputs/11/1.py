
def f1(n, m, board):
    # Initialize the minimum sum to a large value
    min_sum = 10000
    # Loop through all possible values for the 0 cells
    for i in range(1, 2001):
        for j in range(1, 2001):
            # Check if the current value is valid for the Magic Checkerboard
            if is_valid(n, m, board, i, j):
                # Calculate the sum of all values in the Magic Checkerboard
                sum = calculate_sum(n, m, board)
                # Update the minimum sum if necessary
                if sum < min_sum:
                    min_sum = sum
    # Return the minimum sum
    return min_sum

def is_valid(n, m, board, i, j):
    # Check if the current value is valid for the Magic Checkerboard
    for row in range(n):
        for col in range(m):
            if board[row][col] == 0 and row == i and col == j:
                return False
    return True

def calculate_sum(n, m, board):
    # Calculate the sum of all values in the Magic Checkerboard
    sum = 0
    for row in range(n):
        for col in range(m):
            sum += board[row][col]
    return sum

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    print(f1(n, m, board))

