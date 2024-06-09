
def solve(n, a, b):
    # Initialize a dictionary to map each statue to its current and desired island
    statue_map = {i: (a[i], b[i]) for i in range(n)}

    # Initialize a set to keep track of the empty islands
    empty_islands = set(i for i in range(n) if a[i] == 0)

    # Loop until all the statues are in the desired position
    while any(statue_map[i][0] != statue_map[i][1] for i in range(n)):
        # Find the first statue that needs to be moved
        statue_to_move = next((i for i in range(n) if statue_map[i][0] != statue_map[i][1]), None)

        # If no statue needs to be moved, return "NO"
        if statue_to_move is None:
            return "NO"

        # Find the empty island that the statue can be moved to
        empty_island = next(iter(empty_islands))

        # Move the statue to the empty island
        statue_map[empty_island] = (statue_map[statue_to_move][0], statue_map[statue_to_move][1])
        statue_map[statue_to_move] = (0, 0)

        # Update the set of empty islands
        empty_islands.remove(empty_island)
        empty_islands.add(statue_to_move)

    # If all the statues are in the desired position, return "YES"
    return "YES"

