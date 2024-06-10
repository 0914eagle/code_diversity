
def read_input():
    H, W = map(int, input().split())
    A = []
    B = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
        B.append(list(map(int, input().split())))
    return H, W, A, B

def paint_grid(H, W, A, B):
    # Initialize the grid with the given values
    grid = [[(A[i][j], B[i][j]) for j in range(W)] for i in range(H)]
    
    # Paint the grid by alternating the colors
    for i in range(H):
        for j in range(W):
            if i % 2 == 0:
                grid[i][j] = (grid[i][j][0], grid[i][j][1] + 1)
            else:
                grid[i][j] = (grid[i][j][0] + 1, grid[i][j][1])
    
    return grid

def traverse_grid(H, W, grid):
    # Initialize the starting point
    i, j = 0, 0
    
    # Initialize the sum of red and blue numbers
    red_sum, blue_sum = 0, 0
    
    # Traverse the grid
    while i < H and j < W:
        red_sum += grid[i][j][0]
        blue_sum += grid[i][j][1]
        i, j = i + 1, j + 1
    
    return red_sum, blue_sum

def get_unbalancedness(H, W, A, B):
    # Paint the grid
    grid = paint_grid(H, W, A, B)
    
    # Traverse the grid
    red_sum, blue_sum = traverse_grid(H, W, grid)
    
    # Calculate the unbalancedness
    unbalancedness = abs(red_sum - blue_sum)
    
    return unbalancedness

def main():
    H, W, A, B = read_input()
    unbalancedness = get_unbalancedness(H, W, A, B)
    print(unbalancedness)

if __name__ == '__main__':
    main()

