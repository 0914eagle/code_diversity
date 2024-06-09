
def solve(grid, commands):
    # Initialize variables
    start, goal = None, None
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = [(0, 0, 0)]

    # Find the start and goal positions
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "G":
                goal = (i, j)

    # Breadth-first search to find the shortest path from the start to the goal
    while queue:
        i, j, step = queue.pop(0)
        visited.add((i, j))
        if (i, j) == goal:
            return step
        for ii, jj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
            if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] != "#" and (ii, jj) not in visited:
                queue.append((ii, jj, step+1))

    # If the goal is not reachable, return -1
    return -1

