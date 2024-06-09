
def solve(grid, commands):
    # Initialize variables
    start, goal = None, None
    obstacles, empty = set(), set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "G":
                goal = (i, j)
            elif cell == "#":
                obstacles.add((i, j))
            else:
                empty.add((i, j))
    
    # Breadth-first search to find the shortest path from the start to the goal
    queue = [(start, [])]
    visited = set()
    while queue:
        (i, j), path = queue.pop(0)
        if (i, j) == goal:
            return len(path)
        for (ii, jj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if (ii, jj) not in visited and (ii, jj) in empty:
                queue.append(((ii, jj), path + [(ii, jj)]))
                visited.add((ii, jj))
    
    # If no path is found, return -1
    return -1

