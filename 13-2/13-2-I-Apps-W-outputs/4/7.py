
def get_min_operations(table):
    # Initialize variables
    n, m = len(table), len(table[0])
    operations = 0
    visited = set()
    
    # Loop through each cell in the table
    for i in range(n):
        for j in range(m):
            # If the cell is good and has not been visited yet, perform an operation
            if table[i][j] == 1 and (i, j) not in visited:
                operations += 1
                visited.add((i, j))
                # Find all adjacent good cells and mark them as visited
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < m and table[x][y] == 1 and (x, y) not in visited:
                        visited.add((x, y))
    
    return operations

