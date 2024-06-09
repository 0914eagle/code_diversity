
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
                continue
            elif char == '#':
                obstacles.append((i, j))
            elif char == '/' or char == '\\':
                mirrors.append((i, j))
            elif char == 'V':
                gargoyles.append((i, j))
            elif char == 'H':
                gargoyles.append((i, j))
            elif char == 'V' or char == 'H':
                treasure_door = (i, j)

    # Check if the puzzle has a solution
    if not gargoyles or not mirrors or not treasure_door:
        return -1

    # Solve the puzzle using a depth-first search
    visited = set()
    queue = [(0, gargoyles[0])]
    while queue:
        distance, current_gargoyle = queue.pop(0)
        if current_gargoyle == treasure_door:
            return distance
        if current_gargoyle in visited:
            continue
        visited.add(current_gargoyle)
        for mirror in mirrors:
            mirror_distance = distance + 1
            mirror_position = (mirror[0] + current_gargoyle[0], mirror[1] + current_gargoyle[1])
            if mirror_position in obstacles:
                continue
            queue.append((mirror_distance, mirror_position))

    return -1

