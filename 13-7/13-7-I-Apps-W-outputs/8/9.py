
def read_grid():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    return H, W, grid

def paint_grid(H, W, grid):
    # Initialize the grid with all 0s
    painted_grid = [[0] * W for _ in range(H)]
    
    # Paint the first row red
    for j in range(W):
        painted_grid[0][j] = grid[0][j]
    
    # Paint the first column blue
    for i in range(1, H):
        painted_grid[i][0] = grid[i][0]
    
    # Paint the remaining squares
    for i in range(1, H):
        for j in range(1, W):
            if i % 2 == 0:
                painted_grid[i][j] = grid[i][j]
            else:
                painted_grid[i][j] = grid[i][j]
    
    return painted_grid

def get_unbalancedness(H, W, grid):
    painted_grid = paint_grid(H, W, grid)
    red_sum = 0
    blue_sum = 0
    for i in range(H):
        for j in range(W):
            if painted_grid[i][j] == 1:
                red_sum += 1
            else:
                blue_sum += 1
    
    return abs(red_sum - blue_sum)

def main():
    H, W, grid = read_grid()
    print(get_unbalancedness(H, W, grid))

if __name__ == '__main__':
    main()

