
def cakeminator(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    max_cells = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is empty, continue to the next cell
            if grid[i][j] == ".":
                continue

            # If the current cell has an evil strawberry, mark it as visited
            visited = set()
            queue = [(i, j)]
            while queue:
                row, col = queue.pop(0)
                visited.add((row, col))
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and grid[new_row][new_col] == ".":
                        queue.append((new_row, new_col))

            # Update the maximum number of cells visited
            max_cells = max(max_cells, len(visited))

    return max_cells

