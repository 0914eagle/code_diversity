
def solve(n, m, k, table):
    # Initialize variables
    rows, cols = len(table), len(table[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []
    count = 0
    
    # Loop through the table and find connected components
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and table[i][j] == 1:
                # Find the connected component
                component = []
                dfs(i, j, table, visited, component)
                components.append(component)
    
    # Check if it is possible to change k cells
    for component in components:
        if len(component) <= k:
            count += len(component)
        else:
            return -1
    
    return count

# Depth-first search function to find connected components
def dfs(i, j, table, visited, component):
    # Base case
    if i < 0 or i >= len(table) or j < 0 or j >= len(table[0]) or visited[i][j] or table[i][j] == 0:
        return
    
    # Mark the current cell as visited
    visited[i][j] = True
    component.append((i, j))
    
    # Recursive call for the four neighbors
    dfs(i-1, j, table, visited, component)
    dfs(i+1, j, table, visited, component)
    dfs(i, j-1, table, visited, component)
    dfs(i, j+1, table, visited, component)

