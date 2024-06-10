
def read_grid():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    return H, W, A, B

def paint_grid(H, W, A, B):
    # Initialize the grid with all red numbers
    grid = [[1] * W for _ in range(H)]
    
    # Paint the first row and column with blue numbers
    for i in range(W):
        grid[0][i] = 0
    for i in range(H):
        grid[i][0] = 0
    
    # Paint the remaining grid with the minimum unbalancedness
    for i in range(1, H):
        for j in range(1, W):
            grid[i][j] = min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1]) + 1
    
    return grid

def find_min_unbalancedness(H, W, A, B, grid):
    # Calculate the sum of red and blue numbers along the path
    red_sum = 0
    blue_sum = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1:
                red_sum += A[i][j]
            else:
                blue_sum += B[i][j]
    
    # Return the minimum unbalancedness
    return abs(red_sum - blue_sum)

def main():
    H, W, A, B = read_grid()
    grid = paint_grid(H, W, A, B)
    print(find_min_unbalancedness(H, W, A, B, grid))

if __name__ == '__main__':
    main()

