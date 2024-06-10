
def get_input():
    H, W = map(int, input().split())
    assert 1 <= H <= 50 and 1 <= W <= 50
    grid = []
    for _ in range(H):
        row = list(input())
        assert len(row) == W
        grid.append(row)
    return H, W, grid

def paint_black(H, W, grid):
    def is_valid_square(i, j):
        return 0 <= i < H and 0 <= j < W

    def paint_square(i, j):
        if is_valid_square(i, j) and grid[i][j] == '#':
            grid[i][j] = '*'

    def paint_adjacent_squares(i, j):
        paint_square(i, j)
        if is_valid_square(i, j-1):
            paint_square(i, j-1)
        if is_valid_square(i, j+1):
            paint_square(i, j+1)
        if is_valid_square(i-1, j):
            paint_square(i-1, j)
        if is_valid_square(i+1, j):
            paint_square(i+1, j)

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                paint_adjacent_squares(i, j)

    return grid

def is_goal_reached(H, W, grid):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and grid[i][j] != '*':
                return False
    return True

def main():
    H, W, grid = get_input()
    grid = paint_black(H, W, grid)
    if is_goal_reached(H, W, grid):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

