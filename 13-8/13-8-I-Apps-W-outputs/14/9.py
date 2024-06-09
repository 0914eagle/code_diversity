
def solve(N, K, board):
    # Check if the first player can win in one move
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                board[i][j] = 'X'
                if is_winner(N, K, board, 'X'):
                    return "YES"
                board[i][j] = '.'
    
    # If the first player can't win in one move, the second player will win
    return "NO"

def is_winner(N, K, board, symbol):
    # Check rows
    for i in range(N):
        count = 0
        for j in range(N):
            if board[i][j] == symbol:
                count += 1
        if count == K:
            return True
    
    # Check columns
    for j in range(N):
        count = 0
        for i in range(N):
            if board[i][j] == symbol:
                count += 1
        if count == K:
            return True
    
    # Check diagonals
    count = 0
    for i in range(N):
        if board[i][i] == symbol:
            count += 1
    if count == K:
        return True
    
    count = 0
    for i in range(N):
        if board[i][N-i-1] == symbol:
            count += 1
    if count == K:
        return True
    
    return False

