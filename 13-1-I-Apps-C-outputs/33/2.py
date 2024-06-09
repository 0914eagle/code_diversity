
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
    # If the cell has not been visited and is not zero, visit it
    if not visited[i][j] and a[i][j] != 0:
        # Add the cell to the current component
        components[-1].append((i, j))
        # Mark the cell as visited
        visited[i][j] = True
        # Recursively visit the neighboring cells
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            dfs(x, y, value, visited, components)

# Function to check if a component is a rectangle
def is_rectangle(component):
    # If the component is empty, it is not a rectangle
    if not component:
        return False
    # Get the width and height of the rectangle
    width, height = len(component[0]), len(component)
    # Loop through each cell in the component
    for i in range(width):
        for j in range(height):
            # If the cell is not in the component, it is not a rectangle
            if (i, j) not in component:
                return False
    # If all cells are in the component, it is a rectangle
    return True

# Test the function
a = [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 0, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1]]
print(solve(5, 5, 2, a)) # Should be 1

a = [[1, 0, 0, 0],
     [0, 1, 1, 1],
     [1, 1, 1, 0]]
print(solve(3, 4, 1, a)) # Should be -1

a = [[1, 0, 0, 1],
     [0, 1, 1, 0],
     [1, 0, 0, 1]]
print(solve(3, 4, 1, a)) # Should be 0

