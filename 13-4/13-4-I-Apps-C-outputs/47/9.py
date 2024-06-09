
def solve_tomb_puzzle(n, m, floorplan):
    # Initialize variables
    gargoyles = []
    mirrors = []
    obstacles = []
    treasure_door = (0, 0)
    treasure_door_face = None
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
                gargoyles.append((i, j, 'V'))
            elif char == 'H':
                gargoyles.append((i, j, 'H'))
            elif char == 'V' or char == 'H':
                treasure_door = (i, j)
                treasure_door_face = char

    # Check if the treasure door is blocked by an obstacle
    if treasure_door in obstacles:
        return -1

    # Check if the treasure door is facing a gargoyle
    if treasure_door_face == 'V':
        treasure_door_face = 'top'
    elif treasure_door_face == 'H':
        treasure_door_face = 'left'

    # Check if the gargoyles are facing the treasure door
    for gargoyle in gargoyles:
        if gargoyle[2] == treasure_door_face:
            solution.append(gargoyle)

    # Check if the solution is valid
    if len(solution) == len(gargoyles):
        return len(solution)

    # If the solution is not valid, try rotating the gargoyles
    for gargoyle in gargoyles:
        if gargoyle not in solution:
            new_gargoyle = (gargoyle[0], gargoyle[1], 'V' if gargoyle[2] == 'H' else 'H')
            if new_gargoyle not in solution:
                solution.append(new_gargoyle)
                break

    # Check if the solution is valid
    if len(solution) == len(gargoyles):
        return len(solution)

    # If the solution is not valid, return -1
    return -1

