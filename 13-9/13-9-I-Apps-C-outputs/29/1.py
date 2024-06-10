
def get_distances(player, board):
    
    distances = {}
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                distances[(row, col)] = get_distance(player, board, row, col)
    return distances

def get_distance(player, board, row, col):
    
    distances = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player and (i, j) != (row, col):
                distances += get_manhattan_distance(row, col, i, j)
    return distances

def get_manhattan_distance(x1, y1, x2, y2):
    
    return abs(x1 - x2) + abs(y1 - y2)

def get_spread(player, board):
    
    distances = get_distances(player, board)
    spread = 0
    for distance in distances.values():
        spread += distance
    return spread

def main():
    board = []
    for _ in range(int(input())):
        board.append(input())
    mirko_spread = get_spread('M', board)
    slavko_spread = get_spread('S', board)
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

