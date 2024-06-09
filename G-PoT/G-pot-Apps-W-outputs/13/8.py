
t = int(input())

def can_meet(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                knight1 = (i, j)
                break

    for i in range(7, -1, -1):
        for j in range(7, -1, -1):
            if board[i][j] == 'K':
                knight2 = (i, j)
                break

    if (abs(knight1[0] - knight2[0]) % 4 == 0) and (abs(knight1[1] - knight2[1]) % 4 == 0):
        return "YES"
    else:
        return "NO"

for _ in range(t):
    input()  # Skip empty line
    board = [list(input().strip()) for _ in range(8)]
    print(can_meet(board))
