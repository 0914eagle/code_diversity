
def count_subrectangles(grid, j):
    # Initialize a counter for the number of subrectangles with j black cells
    count = 0
    
    # Loop through each subrectangle of size 3x3
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            # Count the number of black cells in the current subrectangle
            black_cells = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if grid[k][l] == 1:
                        black_cells += 1
            
            # If the current subrectangle has j black cells, increment the counter
            if black_cells == j:
                count += 1
    
    return count

def main():
    # Read the input grid
    H, W, N = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append([int(x) for x in input().split()])
    
    # Initialize the counter for each number of black cells
    counts = [0] * 10
    
    # Loop through each number of black cells
    for j in range(10):
        # Count the number of subrectangles with j black cells
        counts[j] = count_subrectangles(grid, j)
    
    # Print the number of subrectangles with each number of black cells
    for j in range(10):
        print(counts[j])

if __name__ == '__main__':
    main()

