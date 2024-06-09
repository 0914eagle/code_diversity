
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = len(a), len(a[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []

    # Loop through each cell
    for i in range(rows):
        for j in range(cols):
            # If the cell has not been visited and its value is 1, start a new component
            if not visited[i][j] and a[i][j] == 1:
                component = []
                dfs(i, j, a, visited, component)
                components.append(component)

    # Loop through each component
    for component in components:
        # If the component is not a rectangle, it is impossible to meet the requirement
        if not is_rectangle(component):
            return -1

        # If the component is a rectangle, check if it can be filled with cells
        if can_fill_rectangle(component, k):
            changed_cells += fill_rectangle(component, a)
            k -= 1

    return changed_cells

# Depth-first search to find all connected components of the same value
def dfs(i, j, a, visited, component):
    # If the cell has not been visited and its value is 1, mark it as visited and add it to the component
    if not visited[i][j] and a[i][j] == 1:
        visited[i][j] = True
        component.append((i, j))

        # Recursively search the neighboring cells
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            dfs(x, y, a, visited, component)

# Check if the component is a rectangle
def is_rectangle(component):
    # If the component is empty, it is not a rectangle
    if not component:
        return False

    # Get the width and height of the component
    width = len(component[0])
    height = len(component)

    # Check if the component is a rectangle by checking if all rows have the same width and all columns have the same height
    for i in range(1, len(component)):
        if len(component[i]) != width:
            return False
    for j in range(width):
        if len(set(row[j] for row in component)) != 1:
            return False

    return True

# Check if the component can be filled with cells
def can_fill_rectangle(component, k):
    # Get the width and height of the component
    width = len(component[0])
    height = len(component)

    # Check if the component can be filled with cells by checking if the number of cells is equal to the product of the width and height
    return k >= width * height

# Fill the component with cells
def fill_rectangle(component, a):
    # Get the width and height of the component
    width = len(component[0])
    height = len(component)

    # Fill the component with cells by setting the value of each cell to 1
    changed_cells = 0
    for i in range(height):
        for j in range(width):
            if a[component[i][j]] == 0:
                a[component[i][j]] = 1
                changed_cells += 1

    return changed_cells

