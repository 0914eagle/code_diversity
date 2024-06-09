
def solve(game_state):
    # Initialize variables
    n, k, board = game_state[0], game_state[1], game_state[2:]
    x_count, o_count = 0, 0
    
    # Iterate over the board
    for i in range(n):
        for j in range(n):
            # Check if the current cell is empty
            if board[i * n + j] == '.':
                # Make a copy of the board
                new_board = list(board)
                # Place an 'X' in the current cell
                new_board[i * n + j] = 'X'
                # Check if the 'X' forms a row, column or diagonal
                if check_row(new_board, k, n, i) or check_column(new_board, k, n, j) or check_diagonal(new_board, k, n, i, j):
                    return "YES"
    
    return "NO"

def check_row(board, k, n, i):
    count = 0
    for j in range(n):
        if board[i * n + j] == 'X':
            count += 1
        elif board[i * n + j] == '.':
            count = 0
        if count == k:
            return True
    return False

def check_column(board, k, n, j):
    count = 0
    for i in range(n):
        if board[i * n + j] == 'X':
            count += 1
        elif board[i * n + j] == '.':
            count = 0
        if count == k:
            return True
    return False

def check_diagonal(board, k, n, i, j):
    count = 0
    for d in range(2 * n - 1):
        x = i + d
        y = j + d
        if x < 0 or y < 0 or x >= n or y >= n:
            break
        if board[x * n + y] == 'X':
            count += 1
        elif board[x * n + y] == '.':
            count = 0
        if count == k:
            return True
    return False

# Main function
if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        n, k = map(int, input().split())
        board = [x for x in input()]
        result = solve((n, k, board))
        print(f"Case #{case}: {result}")

