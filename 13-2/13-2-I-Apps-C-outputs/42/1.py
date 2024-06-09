
def f1(n):
    # Initialize a list to store the safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a safe cell
            if is_safe_cell(i, j, n):
                # Add the cell to the list of safe cells
                safe_cells.append((i, j))

    # Return the list of safe cells
    return safe_cells

def f2(n):
    # Initialize a list to store the safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a safe cell
            if is_safe_cell(i, j, n):
                # Add the cell to the list of safe cells
                safe_cells.append((i, j))

    # Return the list of safe cells
    return safe_cells

def is_safe_cell(i, j, n):
    # Check if the current cell is on the border
    if i == 0 or i == n-1 or j == 0 or j == n-1:
        return False

    # Check if the current cell is adjacent to a mine
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k == i and l == j:
                continue
            if grid[k][l] == 1:
                return False

    # If the current cell is not adjacent to a mine, it is safe
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [[0] * (n+2)] + [[0] + row + [0] for row in [[1] * (n+2)] * n] + [[0] * (n+2)]
    safe_cells = f1(n)
    print(len(safe_cells))
    print(*safe_cells, sep=' ')

