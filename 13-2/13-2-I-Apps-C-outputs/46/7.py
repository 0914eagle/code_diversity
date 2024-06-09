
def f1(Y, X, x_init):
    # Initialize the map and the number of paths
    map = []
    num_paths = 0

    # Read the map from stdin
    for _ in range(Y):
        map.append(list(input()))

    # Check if the ship can move east or west
    can_move_east = False
    can_move_west = False
    for y in range(Y):
        if map[y][x_init] == '>':
            can_move_east = True
        elif map[y][x_init] == '<':
            can_move_west = True

    # Check if the ship can move north
    can_move_north = False
    for x in range(x_init):
        if map[Y-1][x] == '~':
            can_move_north = True
            break

    # Calculate the number of paths
    if can_move_east and can_move_west:
        num_paths += 2
    if can_move_north:
        num_paths += 1

    return num_paths % 1000003

