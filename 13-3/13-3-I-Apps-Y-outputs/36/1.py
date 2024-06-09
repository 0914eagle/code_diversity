
def f1(W, H, map):
    # Initialize variables
    gold_count = 0
    traps_count = 0
    walls_count = 0
    player_position = (0, 0)

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = (i, j)
            elif map[i][j] == 'G':
                gold_count += 1
            elif map[i][j] == 'T':
                traps_count += 1
            elif map[i][j] == '#':
                walls_count += 1

    # Calculate the maximum gold count
    max_gold_count = gold_count - traps_count

    # Return the maximum gold count
    return max_gold_count

def f2(W, H, map):
    # Initialize variables
    gold_count = 0
    traps_count = 0
    walls_count = 0
    player_position = (0, 0)

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = (i, j)
            elif map[i][j] == 'G':
                gold_count += 1
            elif map[i][j] == 'T':
                traps_count += 1
            elif map[i][j] == '#':
                walls_count += 1

    # Calculate the maximum gold count
    max_gold_count = gold_count - traps_count

    # Return the maximum gold count
    return max_gold_count

if __name__ == '__main__':
    W, H = map(int, input().split())
    map = []
    for i in range(H):
        map.append(input())
    print(f1(W, H, map))
    print(f2(W, H, map))

