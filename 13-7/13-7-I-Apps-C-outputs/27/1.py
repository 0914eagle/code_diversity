
def solve(n, m, k, table):
    # Initialize variables
    rows, cols = len(table), len(table[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []
    changed_cells = 0

    # Iterate over the table
    for i in range(rows):
        for j in range(cols):
            # If the current cell is not visited and its value is 1, start a new component
            if not visited[i][j] and table[i][j] == 1:
                component = []
                dfs(i, j, table, visited, component)
                components.append(component)

    # Iterate over the components
    for component in components:
        # If the component is not a rectangle, it is not possible to meet the requirement
        if len(component) != len(set(component)) ** 2:
            return -1

    # If the number of changed cells is less than k, it is possible to meet the requirement
    if changed_cells < k:
        return changed_cells
    else:
        return -1

# Depth-first search function to find all cells in a component
def dfs(i, j, table, visited, component):
    # If the current cell is not visited and its value is 1, mark it as visited and add it to the component
    if not visited[i][j] and table[i][j] == 1:
        visited[i][j] = True
        component.append((i, j))
        # Recursively explore the neighboring cells
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            dfs(ii, jj, table, visited, component)

# Test the function with example inputs
table1 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(solve(5, 5, 2, table1)) # Output: 1

table2 = [[1, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
print(solve(3, 4, 1, table2)) # Output: -1

table3 = [[1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 1]]
print(solve(3, 4, 1, table3)) # Output: 0

