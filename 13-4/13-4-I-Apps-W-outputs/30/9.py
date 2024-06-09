
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
            if board[i][j] == 1 and (i != k or j != n):
                return False
    return True

def add_rows(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 0
                board[i + 1][j] = 1
                return board
    return board

def get_min_rows(board):
    rows = 0
    while not is_good(board):
        board = add_rows(board)
        rows += 1
    return rows

for i in range(m):
    print(get_min_rows(board))

