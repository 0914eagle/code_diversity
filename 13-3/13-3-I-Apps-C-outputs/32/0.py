
def get_minimum_road_cells(map):
    # Initialize variables
    n, m = len(map), len(map[0])
    states = [set() for _ in range(4)]
    visited = [[False] * m for _ in range(n)]
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
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < m and not visited[ii][jj] and map[ii][jj] != '#':
                queue.append((ii, jj))
                visited[ii][jj] = True
                if map[ii][jj].isdigit():
                    states[int(map[ii][jj])].add((ii, jj))

    # Check if all states are connected
    for state in states:
        if not state & states[0]:
            return -1

    # Count the number of cells needed to connect all states
    count = 0
    for state in states:
        for cell in state:
            i, j = cell
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < m and map[ii][jj] != '#' and (ii, jj) not in state:
                    count += 1

    return count

