
def is_objective_achievable(grid):
    
    # Initialize a 2D list to keep track of the painted squares
    painted = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current square is '#', paint it black
            if grid[i][j] == '#':
                painted[i][j] = True
            # If the current square is '.' and its adjacent squares are both painted, paint it black
            elif grid[i][j] == '.' and painted[i][j-1] and painted[i][j+1]:
                painted[i][j] = True
    
    # Check if all the '#' squares are painted
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#' and not painted[i][j]:
                return False
    
    return True

def main():
    
    # Read the input
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    
    # Determine if the objective is achievable
    achievable = is_objective_achievable(grid)
    
    # Print the output
    print("Yes") if achievable else print("No")

if __name__ == '__main__':
    main()

