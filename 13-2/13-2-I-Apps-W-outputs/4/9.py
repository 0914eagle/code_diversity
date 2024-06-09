
def get_min_operations(table):
    # Initialize variables
    n, m = len(table), len(table[0])
    operations = 0
    visited = set()
    
    # Loop through each cell in the table
    for i in range(n):
        for j in range(m):
            # If the cell is good and has not been visited yet, perform a BFS from that cell
            if table[i][j] == 1 and (i, j) not in visited:
                queue = [(i, j)]
                visited.add((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1 and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                operations += 1
    
    return operations

