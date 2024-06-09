
n, k, m = map(int, input().split())

board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    if board[x][y] == 0:
        board[x][y] = 1
    else:
        board[x][y] = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j + 1] += 1
            board[i - 1][j + 1] += 1
            board[i + 1][j + 1] += 1

result = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            result += 1

print(result)

