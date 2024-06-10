
def read_input():
    R, C = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(list(input()))
    return R, C, board

def get_distances(R, C, board):
    distances = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'M':
                distances[i][j] = 1
            elif board[i][j] == 'S':
                distances[i][j] = -1
            else:
                distances[i][j] = 0
    for i in range(R):
        for j in range(C):
            if distances[i][j] != 0:
                for k in range(8):
                    ni = i + (k // 3) - 1
                    nj = j + (k % 3) - 1
                    if 0 <= ni < R and 0 <= nj < C:
                        distances[ni][nj] += distances[i][j]
    return distances

def get_spread(distances):
    spread = 0
    for row in distances:
        for dist in row:
            spread += abs(dist)
    return spread

def main():
    R, C, board = read_input()
    distances = get_distances(R, C, board)
    mirko_spread = get_spread(distances)
    slavko_spread = get_spread([[-d for d in row] for row in distances])
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

