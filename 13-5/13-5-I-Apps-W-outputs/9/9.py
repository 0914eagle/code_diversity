
def get_max_area(grid, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0
    
    # Loop through the sub-rectangle and check if it forms a Nanosoft logo
    for i in range(r1, r2):
        for j in range(c1, c2):
            # Check if the current cell is part of a Nanosoft logo
            if is_nanosoft_logo(grid, i, j):
                # Calculate the area of the sub-square
                area = (i - r1 + 1) * (j - c1 + 1)
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    
    # Return the maximum area
    return max_area

def is_nanosoft_logo(grid, i, j):
    # Check if the current cell is part of a Nanosoft logo
    if grid[i][j] == 'R' and grid[i][j+1] == 'G' and grid[i+1][j] == 'G' and grid[i+1][j+1] == 'B':
        return True
    elif grid[i][j] == 'G' and grid[i][j+1] == 'R' and grid[i+1][j] == 'B' and grid[i+1][j+1] == 'G':
        return True
    elif grid[i][j] == 'B' and grid[i][j+1] == 'G' and grid[i+1][j] == 'G' and grid[i+1][j+1] == 'R':
        return True
    elif grid[i][j] == 'G' and grid[i][j+1] == 'B' and grid[i+1][j] == 'R' and grid[i+1][j+1] == 'G':
        return True
    else:
        return False

def main():
    # Read the input data
    n, m, q = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    
    # Loop through the options
    for i in range(q):
        # Read the option
        r1, c1, r2, c2 = map(int, input().split())
        # Calculate the maximum area
        max_area = get_max_area(grid, r1, c1, r2, c2)
        # Print the result
        print(max_area)

if __name__ == '__main__':
    main()

