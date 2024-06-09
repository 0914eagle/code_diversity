
def solve_tomb_puzzle(n, m, floorplan):
    # Initialize variables
    gargoyles = []
    mirrors = []
    obstacles = []
    treasure_door = []
    solution = []
    visited = []
    queue = []

    # Parse the floorplan and initialize the variables
    for i in range(n):
        for j in range(m):
            char = floorplan[i][j]
            if char == 'V':
                gargoyles.append((i, j))
            elif char == 'H':
                gargoyles.append((i, j))
            elif char == '/' or char == '\\':
                mirrors.append((i, j))
            elif char == '#':
                obstacles.append((i, j))
            elif char == '.':
                treasure_door.append((i, j))

    # Breadth-first search to find the shortest path from the gargoyles to the treasure door
    for gargoyle in gargoyles:
        queue.append(gargoyle)
        visited.append(gargoyle)
        while queue:
            current = queue.pop(0)
            if current == treasure_door:
                return len(visited) - 1
            for neighbor in get_neighbors(current, mirrors, obstacles):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)

    # If no path is found, return -1
    return -1

# Get the neighbors of a cell
def get_neighbors(cell, mirrors, obstacles):
    i, j = cell
    neighbors = []
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if (ni, nj) not in obstacles and (ni, nj) not in mirrors:
            neighbors.append((ni, nj))
        elif (ni, nj) in mirrors:
            for di2, dj2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni2, nj2 = i + di2, j + dj2
                if (ni2, nj2) not in obstacles and (ni2, nj2) not in mirrors:
                    neighbors.append((ni2, nj2))
                    break
    return neighbors

