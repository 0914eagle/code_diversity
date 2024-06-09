
def f1(n):
    # Initialize a list to store the indices of safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a 1
            if grid[i][j] == 1:
                # Check if the cell above, below, left, and right of the current cell are all 0
                if i > 0 and grid[i-1][j] == 0 and grid[i+1][j] == 0 and grid[i][j-1] == 0 and grid[i][j+1] == 0:
                    # If all the surrounding cells are 0, the current cell is safe
                    safe_cells.append(i*n + j + 1)

    return safe_cells

def f2(n):
    # Initialize a list to store the indices of safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a 1
            if grid[i][j] == 1:
                # Check if the cell above, below, left, and right of the current cell are all 0
                if i < n-1 and grid[i+1][j] == 0 and grid[i-1][j] == 0 and grid[i][j-1] == 0 and grid[i][j+1] == 0:
                    # If all the surrounding cells are 0, the current cell is safe
                    safe_cells.append(i*n + j + 1)

    return safe_cells

if __name__ == '__main__':
    n = int(input())
    grid = [[0] * (n+2)] + [[0] + row + [0] for row in [[1] * n] * n] + [[0] * (n+2)]
    safe_cells = f1(n) + f2(n)
    print(len(safe_cells))
    print(*safe_cells)

