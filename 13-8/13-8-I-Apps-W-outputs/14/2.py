
def solve(board, n, k):
    # Check rows
    for i in range(n):
        row = [board[i][j] for j in range(n)]
        if row.count('X') == k and row.count('.') == n - k:
            return "YES"
    
    # Check columns
    for j in range(n):
        column = [board[i][j] for i in range(n)]
        if column.count('X') == k and column.count('.') == n - k:
            return "YES"
    
    # Check diagonals
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' and board[3][3] == 'X' and board[4][4] == 'X':
        return "YES"
    if board[0][4] == 'X' and board[1][3] == 'X' and board[2][2] == 'X' and board[3][1] == 'X' and board[4][0] == 'X':
        return "YES"
    
    return "NO"

