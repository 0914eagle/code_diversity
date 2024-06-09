
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

    # Check if the treasure door is not blocked by an obstacle
    if treasure_door in obstacles:
        return -1

    # Check if there are any gargoyles
    if not gargoyles:
        return 0

    # Check if there are any mirrors
    if not mirrors:
        return -1

    # Initialize the solution with the first gargoyle
    solution.append(gargoyles[0])
    gargoyles.pop(0)

    # Loop until all gargoyles are solved
    while gargoyles:
        # Find the next gargoyle to solve
        next_gargoyle = None
        for gargoyle in gargoyles:
            if gargoyle not in solution:
                next_gargoyle = gargoyle
                break

        # Check if the next gargoyle is blocked by an obstacle
        if next_gargoyle in obstacles:
            return -1

        # Find the mirror that reflects the light from the next gargoyle to the treasure door
        mirror = None
        for m in mirrors:
            if m[0] == next_gargoyle[0] and m[1] == next_gargoyle[1]:
                mirror = m
                break

        # Check if the mirror is blocked by an obstacle
        if mirror in obstacles:
            return -1

        # Add the gargoyle to the solution
        solution.append(next_gargoyle)
        gargoyles.pop(gargoyles.index(next_gargoyle))

        # Add the mirror to the solution
        solution.append(mirror)
        mirrors.pop(mirrors.index(mirror))

    # Return the number of gargoyles that have to be rotated
    return len(solution) // 2

