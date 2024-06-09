
def f1(map):
    # Initialize variables
    gold = 0
    traps = 0
    walls = 0
    player_position = []

    # Parse the map
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == 'P':
                player_position = [i, j]
            elif char == 'G':
                gold += 1
            elif char == 'T':
                traps += 1
            elif char == '#':
                walls += 1

    # Calculate the maximum gold the player can get
    max_gold = gold - traps

    # Return the maximum gold
    return max_gold

def f2(map):
    # Initialize variables
    gold = 0
    traps = 0
    walls = 0
    player_position = []

    # Parse the map
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == 'P':
                player_position = [i, j]
            elif char == 'G':
                gold += 1
            elif char == 'T':
                traps += 1
            elif char == '#':
                walls += 1

    # Calculate the maximum gold the player can get
    max_gold = gold - traps

    # Return the maximum gold
    return max_gold

if __name__ == '__main__':
    map = [
        '#######',
        '#P.GTG#',
        '#..TGG#',
        '#######'
    ]
    print(f1(map))
    print(f2(map))

