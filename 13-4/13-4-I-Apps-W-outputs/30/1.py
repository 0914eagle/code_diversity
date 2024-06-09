
n, k, m = map(int, input().split())

board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    if board[x][y] == 0:
        board[x][y] = 1
    else:
        board[x][y] = 0

def is_good():
    for i in range(n + 1):
        for j in range(n + 1):
            if board[i][j] == 1 and (i != k or j != 1):
                return False
    return True

def add_rows():
    count = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if board[i][j] == 1 and i != k and j != 1:
                board[i][j] = 0
                board[i + count][j] = 1
                count += 1
    return count

while not is_good():
    print(add_rows())

