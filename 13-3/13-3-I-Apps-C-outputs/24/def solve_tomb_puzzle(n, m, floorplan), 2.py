
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
            if char == '.':
                pass
            elif char == '#':
                obstacles.append((i, j))
            elif char == '/' or char == '\\':
                mirrors.append((i, j))
            elif char == 'V':
                gargoyles.append((i, j))
            elif char == 'H':
                gargoyles.append((i, j))
            elif char == 'V':
                treasure_door = (i, j)

    # Check if the treasure door is reachable
    if not is_reachable(treasure_door, obstacles):
        return -1

    # Find the shortest path to the treasure door
    path = find_path(treasure_door, obstacles)

    # Rotate the gargoyles to form a path to the treasure door
    for gargoyle in gargoyles:
        if not is_reachable(gargoyle, obstacles):
            continue
        path_to_gargoyle = find_path(gargoyle, obstacles)
        if path_to_gargoyle is not None:
            solution.append(gargoyle)
            obstacles.append(gargoyle)
            path = path_to_gargoyle

    return len(solution)

def is_reachable(position, obstacles):
    queue = [position]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if current in obstacles:
            return False
        if current == (0, 0):
            return True
        queue.extend(get_neighbors(current, obstacles))
    return False

def find_path(start, obstacles):
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if current == (0, 0):
            return queue
        queue.extend(get_neighbors(current, obstacles))
    return None

def get_neighbors(position, obstacles):
    neighbors = []
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor = (position[0] + x, position[1] + y)
        if neighbor not in obstacles:
            neighbors.append(neighbor)
    return neighbors

