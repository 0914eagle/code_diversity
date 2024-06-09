
def solve(vault):
    # Initialize variables
    m, n = len(vault), len(vault[0])
    visited = [[False] * n for _ in range(m)]
    queue = [(0, 0, 0)]

    # Breadth-first search
    while queue:
        i, j, ladder_length = queue.pop(0)

        # If we have reached the last row and column, return the ladder length
        if i == m - 1 and j == n - 1:
            return ladder_length

        # Visit all the adjacent cells and add them to the queue if they have not been visited before
        for ii, jj in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= ii < m and 0 <= jj < n and not visited[ii][jj]:
                visited[ii][jj] = True
                queue.append((ii, jj, max(ladder_length, abs(vault[ii][jj] - vault[i][j]))))

    # If we reach this point, it means that we could not find a way to reach the last row and column
    return -1

