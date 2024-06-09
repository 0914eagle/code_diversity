
def f1(H, W, grid):
    # Initialize the number of even cells to 0
    num_even_cells = 0
    
    # Loop through each cell in the grid
    for i in range(H):
        for j in range(W):
            # If the current cell contains an even number of coins, increment the number of even cells
            if grid[i][j] % 2 == 0:
                num_even_cells += 1
    
    # Return the number of even cells
    return num_even_cells

def f2(H, W, grid):
    # Initialize the number of operations to 0
    num_operations = 0
    
    # Loop through each cell in the grid
    for i in range(H):
        for j in range(W):
            # If the current cell contains an odd number of coins, increment the number of operations
            if grid[i][j] % 2 == 1:
                num_operations += 1
    
    # Return the number of operations
    return num_operations

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    
    # Call f1 and f2 to get the number of even cells and operations respectively
    num_even_cells = f1(H, W, grid)
    num_operations = f2(H, W, grid)
    
    # Print the number of operations
    print(num_operations)
    
    # Loop through each cell in the grid
    for i in range(H):
        for j in range(W):
            # If the current cell contains an odd number of coins, print the operation to move one of the coins to a vertically or horizontally adjacent cell
            if grid[i][j] % 2 == 1:
                print(i+1, j+1, i+1, j+2)

