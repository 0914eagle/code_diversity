_tank(board, tank, target_row, target_col):
    moves = []
    current_row, current_col = tank
    while current_row != target_row:
        if current_row < target_row:
            current_row += 1
            moves.append('D')
        else:
            current_row -= 1
            moves.append('U')
    while current_col != target_col:
        if current_col < target_col:
            current_col += 1
            moves.append('R')
        else:
            current_col -= 1
            moves.append('L')
    board[current_row][current_col] = tank
    return moves

def rearrange_tanks(N, tanks):
    board = [[0] * N for _ in range(N)]
    for i, tank in enumerate(tanks, 1):
        row, col = tank
        board[row - 1][col - 1] = i

    moves = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                moves += move_tank(board, board[i][j], i, j)

    return moves

if __name__ == "__main__":
    N = int(input())
    tanks = [list(map(int, input().split())) for _ in range(N)]
    
    moves = rearrange_tanks(N, tanks)
    
    print(len(moves))
    for move in moves:
        print(move