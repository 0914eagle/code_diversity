
n, k, m = map(int, input().split())

board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    if board[x][y] == 0:
        board[x][y] = 1
    else:
        board[x][y] = 0

def is_good(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and (i != k or j != 1):
                return False
    return True

def add_rows(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i + 1][j] = 1
                board[i][j] = 0
    return board

def solve(board):
    while not is_good(board):
        board = add_rows(board)
    return board

board = solve(board)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            print(i - k + 1)
            break
    else:
        print(0)

