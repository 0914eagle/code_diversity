
def get_subrectangles(grid):
    # Initialize a dictionary to store the number of subrectangles for each number of black cells
    subrectangles = {i: 0 for i in range(10)}
    
    # Loop through the grid and count the number of subrectangles for each number of black cells
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            black_cells = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if grid[k][l] == 1:
                        black_cells += 1
            subrectangles[black_cells] += 1
    
    return subrectangles

def main():
    # Read the input grid
    H, W, N = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    
    # Get the number of subrectangles for each number of black cells
    subrectangles = get_subrectangles(grid)
    
    # Print the number of subrectangles for each number of black cells
    for i in range(10):
        print(subrectangles[i])

if __name__ == '__main__':
    main()

