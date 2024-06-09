
def solve(board, k):
    # Check rows
    for row in board:
        if row.count('X') == k:
            return "YES"
    
    # Check columns
    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if col.count('X') == k:
            return "YES"
    
    # Check diagonals
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return "YES"
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return "YES"
    
    return "NO"

