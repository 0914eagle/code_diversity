
def get_board(rows, cols):
    board = []
    for i in range(rows):
        board.append(list(input()))
    return board

def get_spread(board, player):
    spread = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                spread += get_distance(board, i, j, player)
    return spread

def get_distance(board, row, col, player):
    distance = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if board[i][j] == player:
                    distance += 1
    return distance

def main():
    rows, cols = map(int, input().split())
    board = get_board(rows, cols)
    mirko_spread = get_spread(board, 'M')
    slavko_spread = get_spread(board, 'S')
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

