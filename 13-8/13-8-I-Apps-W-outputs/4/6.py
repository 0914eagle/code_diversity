
def solve(grid):
    # Initialize variables
    rows = len(grid)
    cols = len(grid[0])
    max_cells = 0

    # Loop through each row and column
    for i in range(rows):
        for j in range(cols):
            # If the current cell is empty, continue to the next cell
            if grid[i][j] == '.':
                continue

            # If the current cell is an evil strawberry, mark it as visited
            visited = set()
            visited.add((i, j))

            # Find all the adjacent empty cells and mark them as visited
            queue = [(i, j)]
            while queue:
                row, col = queue.pop(0)
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '.' and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))

            # Update the maximum number of cells if necessary
            max_cells = max(max_cells, len(visited))

    return max_cells

