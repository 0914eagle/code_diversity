
def solve(game_board, k):
    # Check rows
    for row in game_board:
        if row.count('X') == k:
            return "YES"
    
    # Check columns
    for i in range(len(game_board[0])):
        col = [row[i] for row in game_board]
        if col.count('X') == k:
            return "YES"
    
    # Check diagonals
    if game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X':
        return "YES"
    if game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X':
        return "YES"
    
    return "NO"

