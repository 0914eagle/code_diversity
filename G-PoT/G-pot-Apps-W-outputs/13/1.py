
t = int(input())

def can_meet(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                knight1 = (i, j)
                board[i][j] = '.'
            elif board[i][j] == 'K':
                knight2 = (i, j)
                board[i][j] = '.'

    if abs(knight1[0] - knight2[0]) % 4 == 0 and abs(knight1[1] - knight2[1]) % 4 == 0:
        return "YES"
    else:
        return "NO"

for _ in range(t):
    board = [list(input()) for _ in range(8)]
    input()  # Skip empty line
    print(can_meet(board))
