
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = len(a), len(a[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []

    # Loop through each cell and check if it is connected to any other cell with the same value
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and a[i][j] == 1:
                # If the cell is not visited and has value 1, start a new component
                component = []
                dfs(i, j, a, visited, component)
                components.append(component)

    # Check if any component forms a rectangle with sides parallel to the sides of the table
    for component in components:
        if len(component) == rows * cols:
            # If the component contains all the cells, it forms a rectangle with sides parallel to the sides of the table
            return 0

    # If no component forms a rectangle with sides parallel to the sides of the table, check if it is possible to change at most k cells to form a rectangle
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and a[i][j] == 0 and changed_cells < k:
                # If the cell is not visited and has value 0, change its value to 1 and increment the number of changed cells
                a[i][j] = 1
                changed_cells += 1
                dfs(i, j, a, visited, [])

    # If it is not possible to change at most k cells to form a rectangle, return -1
    if changed_cells > k:
        return -1

    # If it is possible to change at most k cells to form a rectangle, return the minimum number of cells that should be changed
    return changed_cells

# Depth-first search function to check if a cell is connected to any other cell with the same value
def dfs(i, j, a, visited, component):
    if 0 <= i < len(a) and 0 <= j < len(a[0]) and not visited[i][j] and a[i][j] == 1:
        visited[i][j] = True
        component.append((i, j))
        dfs(i-1, j, a, visited, component)
        dfs(i+1, j, a, visited, component)
        dfs(i, j-1, a, visited, component)
        dfs(i, j+1, a, visited, component)

