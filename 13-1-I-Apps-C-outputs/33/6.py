
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = len(a), len(a[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []

    # Loop through each cell
    for i in range(rows):
        for j in range(cols):
            # If the cell has not been visited and is not zero, visit it
            if not visited[i][j] and a[i][j] != 0:
                # DFS to find all connected components with the same value
                dfs(i, j, a[i][j], visited, components)

    # Loop through each component
    for component in components:
        # If the component is not a rectangle, it is not possible to meet the requirement
        if not is_rectangle(component):
            return -1

    # If we have not used up all of our changes, return -1
    if changed_cells > k:
        return -1

    # Return the minimum number of cells that need to be changed
    return k - changed_cells

# DFS function to find all connected components with the same value
def dfs(i, j, value, visited, components):
    # If the cell has already been visited, return
    if visited[i][j]:
        return

    # Mark the cell as visited and add it to the current component
    visited[i][j] = True
    components[-1].append((i, j))

    # Recursively visit the neighboring cells
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < len(visited) and 0 <= y < len(visited[0]) and visited[x][y] == False and a[x][y] == value:
            dfs(x, y, value, visited, components)

# Function to check if a component is a rectangle
def is_rectangle(component):
    # If the component is empty, return True
    if len(component) == 0:
        return True

    # Get the x and y coordinates of the component
    x_coords = [x for x, _ in component]
    y_coords = [y for _, y in component]

    # Get the minimum and maximum x and y coordinates
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)

    # Check if the component is a rectangle by checking if all x coordinates are the same and all y coordinates are the same
    return all(x == min_x for x in x_coords) and all(y == min_y for y in y_coords) and all(x == max_x for x in x_coords) and all(y == max_y for y in y_coords)

