
def f1(W, H, map):
    # Initialize variables
    gold_count = 0
    traps_count = 0
    walls_count = 0
    player_position = []
    gold_positions = []
    trap_positions = []
    wall_positions = []

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = [i, j]
            elif map[i][j] == 'G':
                gold_positions.append([i, j])
            elif map[i][j] == 'T':
                trap_positions.append([i, j])
            elif map[i][j] == '#':
                wall_positions.append([i, j])

    # Calculate the number of gold the player can get
    for gold in gold_positions:
        if gold not in trap_positions and gold not in wall_positions:
            gold_count += 1

    return gold_count

def f2(W, H, map):
    # Initialize variables
    gold_count = 0
    traps_count = 0
    walls_count = 0
    player_position = []
    gold_positions = []
    trap_positions = []
    wall_positions = []

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = [i, j]
            elif map[i][j] == 'G':
                gold_positions.append([i, j])
            elif map[i][j] == 'T':
                trap_positions.append([i, j])
            elif map[i][j] == '#':
                wall_positions.append([i, j])

    # Calculate the number of gold the player can get
    for gold in gold_positions:
        if gold not in trap_positions and gold not in wall_positions:
            gold_count += 1

    return gold_count

if __name__ == '__main__':
    W, H = map(int, input().split())
    map = []
    for i in range(H):
        map.append(input())
    print(f1(W, H, map))
    print(f2(W, H, map))

