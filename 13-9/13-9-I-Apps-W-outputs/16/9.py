
def check_2x2_square(board):
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):
            if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
                return True
    return False

def check_moves(board, moves):
    for move in moves:
        row, col = move
        board[row - 1][col - 1] = 1
        if check_2x2_square(board):
            return move
    return 0

def main():
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    moves = []
    for _ in range(k):
        moves.append(list(map(int, input().split())))
    result = check_moves(board, moves)
    print(result)

if __name__ == '__main__':
    main()

