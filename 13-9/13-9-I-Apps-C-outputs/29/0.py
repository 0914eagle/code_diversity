
def get_distance(mirko_row, mirko_col, slavko_row, slavko_col):
    return abs(mirko_row - slavko_row) + abs(mirko_col - slavko_col)

def get_spread(board, player):
    spread = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                for k in range(len(board)):
                    for l in range(len(board[0])):
                        if board[k][l] == player:
                            spread += get_distance(i, j, k, l)
    return spread

def main():
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]
    mirko_spread = get_spread(board, 'M')
    slavko_spread = get_spread(board, 'S')
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

