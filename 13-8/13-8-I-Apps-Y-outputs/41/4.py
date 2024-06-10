
def get_input():
    H, W = map(int, input().split())
    squares = []
    for _ in range(H):
        squares.append(list(input()))
    return H, W, squares

def is_valid_position(H, W, pos):
    i, j = pos
    return 0 <= i < H and 0 <= j < W

def paint(H, W, squares, pos, color):
    i, j = pos
    if not is_valid_position(H, W, pos) or squares[i][j] == color:
        return
    squares[i][j] = color
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        paint(H, W, squares, (x, y), color)

def is_objective_achievable(H, W, squares):
    for i in range(H):
        for j in range(W):
            if squares[i][j] == '#':
                paint(H, W, squares, (i, j), '#')
    for i in range(H):
        for j in range(W):
            if squares[i][j] == '.':
                return False
    return True

def main():
    H, W, squares = get_input()
    print("Yes" if is_objective_achievable(H, W, squares) else "No")

if __name__ == '__main__':
    main()

