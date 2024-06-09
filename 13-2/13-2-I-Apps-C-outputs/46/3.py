
def f1(Y, X, x_init):
    # Initialize the map and the number of paths
    map = []
    paths = 0

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
    for x in range(X):
        if map[Y-1][x] == '~':
            can_move_north = True
            break

    # Calculate the number of paths
    if can_move_east and can_move_west:
        paths += 2
    if can_move_north:
        paths += 1

    return paths % 1000003

def f2(Y, X, x_init):
    # Initialize the map and the number of paths
    map = []
    paths = 0

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
    for x in range(X):
        if map[Y-1][x] == '~':
            can_move_north = True
            break

    # Calculate the number of paths
    if can_move_east and can_move_west:
        paths += 2
    if can_move_north:
        paths += 1

    return paths % 1000003

if __name__ == '__main__':
    Y = int(input())
    X = int(input())
    x_init = int(input())
    print(f1(Y, X, x_init))
    print(f2(Y, X, x_init))

