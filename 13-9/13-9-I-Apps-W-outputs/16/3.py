
def check_moves(n, m, k, moves):
    board = [[0] * m for _ in range(n)]
    for i in range(k):
        row, col = moves[i]
        board[row - 1][col - 1] = 1
        if board[row - 1][col - 1] == 1 and (board[row - 1][col] == 1 or board[row][col - 1] == 1):
            return i + 1
    return 0

def main():
    n, m, k = map(int, input().split())
    moves = []
    for i in range(k):
        moves.append(list(map(int, input().split())))
    result = check_moves(n, m, k, moves)
    print(result)

if __name__ == '__main__':
    main()

