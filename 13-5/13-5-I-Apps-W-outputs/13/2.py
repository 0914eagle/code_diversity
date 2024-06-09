
def count_subrectangles(grid, j):
    # Initialize a counter for the number of subrectangles
    count = 0
    
    # Iterate over the grid
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            # Count the number of black cells in the current subrectangle
            black_cells = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if grid[k][l] == 1:
                        black_cells += 1
            
            # If the number of black cells is equal to j, increment the counter
            if black_cells == j:
                count += 1
    
    return count

def main():
    # Read the input grid
    H, W, N = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    
    # Initialize the counter for each value of j
    counts = [0] * 10
    
    # Iterate over the values of j
    for j in range(10):
        # Count the number of subrectangles that contain exactly j black cells
        counts[j] = count_subrectangles(grid, j)
    
    # Print the counts
    for count in counts:
        print(count)

if __name__ == '__main__':
    main()

