
n, m = map(int, input().split())

board = [[0] * n for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

    # Count the number of cells not under attack
    count = 0
    for row in board:
        count += row.count(0)
    print(count)

