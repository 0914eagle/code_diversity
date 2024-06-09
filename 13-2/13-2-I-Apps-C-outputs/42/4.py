
def f1(n):
    # Initialize a list to store the safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a safe cell
            if is_safe_cell(i, j, n):
                # Add the current cell to the list of safe cells
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
                # Add the current cell to the list of safe cells
                safe_cells.append((i, j))

    # Return the list of safe cells
    return safe_cells

def is_safe_cell(i, j, n):
    # Check if the current cell is on the border
    if i == 0 or i == n-1 or j == 0 or j == n-1:
        return False

    # Check if the current cell has a mine in any of its neighbors
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            if grid[i+di][j+dj] == 1:
                return False

    # If the current cell has no mines in its neighbors, it is a safe cell
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [[0] * (n+2)] + [[1] + [0] * n + [1] for _ in range(n)] + [[0] * (n+2)]
    safe_cells = f1(n)
    print(len(safe_cells))
    print(*safe_cells, sep=' ')

