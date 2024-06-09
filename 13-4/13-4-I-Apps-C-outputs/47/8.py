
def solve_tomb_puzzle(n, m, floorplan):
    # Initialize variables
    gargoyles = []
    mirrors = []
    obstacles = []
    treasure_door = (0, 0)
    solution = []

    # Parse the floorplan
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
                treasure_door = (i, j)

    # Check if the treasure door is reachable
    if not is_reachable(treasure_door, gargoyles, mirrors, obstacles):
        return -1

    # Rotate the gargoyles to solve the puzzle
    for g in gargoyles:
        if not is_reachable(g, gargoyles, mirrors, obstacles):
            solution.append(g)

    return len(solution)

def is_reachable(start, gargoyles, mirrors, obstacles):
    # Initialize variables
    queue = [(start, 0)]
    visited = set()

    # Breadth-first search
    while queue:
        current, distance = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if current == treasure_door:
            return True
        for neighbor in get_neighbors(current, gargoyles, mirrors, obstacles):
            queue.append((neighbor, distance + 1))
    return False

def get_neighbors(current, gargoyles, mirrors, obstacles):
    # Initialize variables
    neighbors = []

    # Get the neighbors of the current cell
    for i in range(current[0] - 1, current[0] + 2):
        for j in range(current[1] - 1, current[1] + 2):
            if (i, j) != current and (i, j) not in visited:
                neighbors.append((i, j))

    # Check if the neighbors are valid
    valid_neighbors = []
    for neighbor in neighbors:
        if neighbor in gargoyles or neighbor in mirrors or neighbor in obstacles:
            continue
        valid_neighbors.append(neighbor)

    return valid_neighbors

