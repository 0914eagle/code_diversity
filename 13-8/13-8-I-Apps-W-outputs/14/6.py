
def solve(board, k, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                if is_winning_move(board, k, n, i, j):
                    return "YES"
    return "NO"

def is_winning_move(board, k, n, i, j):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            count = 1
            ii = i + di
            jj = j + dj
            while ii >= 0 and ii < n and jj >= 0 and jj < n and board[ii][jj] == 'X':
                count += 1
                ii += di
                jj += dj
            if count >= k:
                return True
    return False

