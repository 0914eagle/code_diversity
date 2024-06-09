
def f1(W, H, map):
    # Initialize variables
    gold = 0
    traps = 0
    walls = 0
    player_position = None

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = (i, j)
            elif map[i][j] == 'G':
                gold += 1
            elif map[i][j] == 'T':
                traps += 1
            elif map[i][j] == '#':
                walls += 1

    # Calculate the maximum gold the player can get
    max_gold = gold - traps

    # Return the maximum gold
    return max_gold

def f2(W, H, map):
    # Initialize variables
    gold = 0
    traps = 0
    walls = 0
    player_position = None

    # Parse the map
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'P':
                player_position = (i, j)
            elif map[i][j] == 'G':
                gold += 1
            elif map[i][j] == 'T':
                traps += 1
            elif map[i][j] == '#':
                walls += 1

    # Calculate the maximum gold the player can get
    max_gold = gold - traps

    # Return the maximum gold
    return max_gold

if __name__ == '__main__':
    W, H = map(int, input().split())
    map = []
    for i in range(H):
        map.append(input())
    print(f1(W, H, map))
    print(f2(W, H, map))

