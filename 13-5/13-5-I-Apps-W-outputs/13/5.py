
def get_subrectangles(grid):
    # Initialize a dictionary to store the number of subrectangles for each number of black cells
    subrectangles = {i: 0 for i in range(10)}
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current cell is black, increment the number of subrectangles for each number of black cells
            if grid[i][j] == 1:
                for k in range(1, 10):
                    subrectangles[k] += 1
    
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

