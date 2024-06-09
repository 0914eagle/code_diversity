
def get_max_points(N, E, S_X, S_Y, C, cans):
    # Initialize a 2D array to store the number of points at each cell
    points = [[0] * N for _ in range(N)]

    # Loop through each can and its appearance time
    for can in cans:
        x, y, t = can
        # If the can appears before Johnny5 reaches the cell, increase the number of points at that cell
        if t < S_X + S_Y:
            points[x][y] += 1

    # Loop through each cell and its neighbors
    for x in range(N):
        for y in range(N):
            # If the cell has at least one point, check if any of its neighbors have a point
            if points[x][y] > 0:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # If the neighbor has a point, increase the number of points at the current cell
                    if 0 <= nx < N and 0 <= ny < N and points[nx][ny] > 0:
                        points[x][y] += 1

    # Return the maximum number of points
    return max(sum(row) for row in points)

