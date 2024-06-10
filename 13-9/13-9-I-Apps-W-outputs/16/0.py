
def read_input():
    n, m, k = map(int, input().split())
    moves = []
    for _ in range(k):
        moves.append(tuple(map(int, input().split())))
    return n, m, k, moves

def check_losing_move(n, m, k, moves):
    board = [[0] * m for _ in range(n)]
    for i, j in moves:
        board[i - 1][j - 1] = 1
        if board[i - 1][j - 1] == 1 and board[i - 1][j] == 1 and board[i][j - 1] == 1:
            return k
    return 0

def main():
    n, m, k, moves = read_input()
    print(check_losing_move(n, m, k, moves))

if __name__ == '__main__':
    main()

