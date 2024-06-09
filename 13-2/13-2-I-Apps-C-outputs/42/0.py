
def f1(n):
    # Initialize a list to store the indices of safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a safe cell
            if is_safe_cell(i, j, n):
                # Add the index of the safe cell to the list
                safe_cells.append((i * n) + j + 1)

    # Return the number of safe cells and their indices
    return len(safe_cells), safe_cells

def f2(n):
    # Initialize a list to store the indices of safe cells
    safe_cells = []

    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # Check if the current cell is a safe cell
            if is_safe_cell(i, j, n):
                # Add the index of the safe cell to the list
                safe_cells.append((i * n) + j + 1)

    # Return the number of safe cells and their indices
    return len(safe_cells), safe_cells

def is_safe_cell(i, j, n):
    # Check if the current cell is on the border
    if i == 0 or i == n - 1 or j == 0 or j == n - 1:
        return True

    # Check if the current cell has a mine in any of its adjacent cells
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if row == i and col == j:
                continue
            if grid[row][col] == 1:
                return False

    # If the current cell has no mines in its adjacent cells, it is a safe cell
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = int(input())
    m, safe_cells = f1(n)
    print(m)
    print(*safe_cells)

