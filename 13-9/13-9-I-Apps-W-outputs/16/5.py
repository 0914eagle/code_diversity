
def is_losing_move(move, n, m, pixels):
    i, j = move
    if pixels[i][j] == 1:
        return True
    pixels[i][j] = 1
    if i > 0 and pixels[i-1][j] == 1 and j > 0 and pixels[i][j-1] == 1:
        return True
    if i < n-1 and pixels[i+1][j] == 1 and j < m-1 and pixels[i][j+1] == 1:
        return True
    if i > 0 and pixels[i-1][j] == 1 and j < m-1 and pixels[i][j+1] == 1:
        return True
    if i < n-1 and pixels[i+1][j] == 1 and j > 0 and pixels[i][j-1] == 1:
        return True
    return False

def find_losing_move(moves, n, m):
    pixels = [[0 for _ in range(m)] for _ in range(n)]
    for move in moves:
        if is_losing_move(move, n, m, pixels):
            return moves.index(move) + 1
    return 0

def main():
    n, m, k = map(int, input().split())
    moves = [tuple(map(int, input().split())) for _ in range(k)]
    print(find_losing_move(moves, n, m))

if __name__ == '__main__':
    main()

