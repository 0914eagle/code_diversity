
def shortest_ladder(vault):
    # Initialize variables
    m, n = len(vault), len(vault[0])
    visited = [[False] * n for _ in range(m)]
    queue = [(0, 0, 0)]

    # Direction vectors
    dr = [0, 1, 0, -1, 0]
    dc = [1, 0, 0, 0, -1]

    # BFS to find shortest path
    while queue:
        r, c, dist = queue.pop(0)

        if visited[r][c]:
            continue

        visited[r][c] = True

        if r == m - 1 and c == n - 1:
            return dist

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < m and 0 <= nc < n:
                queue.append((nr, nc, dist + 1))

    return -1

