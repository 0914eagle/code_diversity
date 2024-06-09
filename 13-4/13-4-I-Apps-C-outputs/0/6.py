
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

        # If the current position is the goal, return the number of steps
        if i == goal[0] and j == goal[1]:
            return step

        # If the current position is already visited, skip it
        if (i, j) in visited:
            continue

        # Mark the current position as visited
        visited.add((i, j))

        # Add the neighbors to the queue
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] != "#":
                queue.append((x, y, step+1))

    # If the goal is not found, return -1
    return -1

