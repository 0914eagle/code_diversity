
def f1(Y, X, x_init):
    # Initialize the map and the number of paths
    map = [[0] * X for _ in range(Y)]
    num_paths = 0
    
    # Fill in the map with the given data
    for y in range(Y):
        for x in range(X):
            map[y][x] = input()
    
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
    
    # Check if the ship can move south
    can_move_south = False
    for x in range(X):
        if map[0][x] == '~':
            can_move_south = True
            break
    
    # Count the number of paths
    if can_move_east:
        num_paths += 1
    if can_move_west:
        num_paths += 1
    if can_move_north:
        num_paths += 1
    if can_move_south:
        num_paths += 1
    
    # Return the number of paths
    return num_paths % 1000003

def f2(Y, X, x_init):
    # Initialize the map and the number of paths
    map = [[0] * X for _ in range(Y)]
    num_paths = 0
    
    # Fill in the map with the given data
    for y in range(Y):
        for x in range(X):
            map[y][x] = input()
    
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
    
    # Check if the ship can move south
    can_move_south = False
    for x in range(X):
        if map[0][x] == '~':
            can_move_south = True
            break
    
    # Count the number of paths
    if can_move_east:
        num_paths += 1
    if can_move_west:
        num_paths += 1
    if can_move_north:
        num_paths += 1
    if can_move_south:
        num_paths += 1
    
    # Return the number of paths
    return num_paths % 1000003

if __name__ == '__main__':
    Y = int(input())
    X = int(input())
    x_init = int(input())
    print(f1(Y, X, x_init))
    print(f2(Y, X, x_init))

