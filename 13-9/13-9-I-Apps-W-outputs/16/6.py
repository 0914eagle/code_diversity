
def get_black_squares(n, m, k, moves):
    board = [[0] * m for _ in range(n)]
    for i, j in moves:
        board[i - 1][j - 1] = 1
    for i in range(n - 1):
        for j in range(m - 1):
            if board[i][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j] == 1 and board[i + 1][j + 1] == 1:
                return k
    return 0

def main():
    n, m, k = map(int, input().split())
    moves = []
    for _ in range(k):
        moves.append(list(map(int, input().split())))
    print(get_black_squares(n, m, k, moves))

if __name__ == '__main__':
    main()

