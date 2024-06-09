
def get_minimum_road_cells(map):
    # Initialize variables
    n, m = len(map), len(map[0])
    states = [set() for _ in range(4)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = []
    
    # Populate the states and visited arrays
    for i in range(n):
        for j in range(m):
            if map[i][j].isdigit():
                states[int(map[i][j])].add((i, j))
            elif map[i][j] == '.':
                queue.append((i, j))
                visited[i][j] = True
    
    # Breadth-first search to find the minimum number of cells needed to connect all states
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and map[ni][nj] != '#':
                queue.append((ni, nj))
                visited[ni][nj] = True
                for state in states:
                    if (ni, nj) in state:
                        state.remove((ni, nj))
                        if not state:
                            return len(queue)
    
    # If all states are not connected, return -1
    return -1

