
def solve(N, K, board):
    # Check if the current player can win in one move
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                if can_win_in_one_move(N, K, board, i, j):
                    return "YES"
    
    # Check if the other player can win in one move
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                board[i][j] = 'O'
                if can_win_in_one_move(N, K, board, i, j):
                    return "NO"
                board[i][j] = '.'
    
    # If no one can win in one move, return "NO"
    return "NO"

def can_win_in_one_move(N, K, board, i, j):
    # Check rows
    for k in range(N):
        count = 0
        for l in range(N):
            if board[k][l] == 'X':
                count += 1
                if count == K:
                    return True
            else:
                count = 0
    
    # Check columns
    for k in range(N):
        count = 0
        for l in range(N):
            if board[l][k] == 'X':
                count += 1
                if count == K:
                    return True
            else:
                count = 0
    
    # Check diagonals
    count = 0
    for k in range(N):
        if board[k][k] == 'X':
            count += 1
            if count == K:
                return True
        else:
            count = 0
    
    count = 0
    for k in range(N):
        if board[k][N-k-1] == 'X':
            count += 1
            if count == K:
                return True
        else:
            count = 0
    
    return False

