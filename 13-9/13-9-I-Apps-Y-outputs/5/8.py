
def get_gold_safe(map):
    # Initialize variables
    gold_count = 0
    trap_count = 0
    player_position = []
    wall_position = []
    
    # Parse the map
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col == 'P':
                player_position = [i, j]
            elif col == 'G':
                gold_count += 1
            elif col == 'T':
                trap_count += 1
            elif col == '#':
                wall_position.append([i, j])
    
    # Calculate the safe gold count
    safe_gold_count = 0
    for i in range(player_position[0] - trap_count, player_position[0] + trap_count + 1):
        for j in range(player_position[1] - trap_count, player_position[1] + trap_count + 1):
            if [i, j] in wall_position:
                continue
            safe_gold_count += 1
    
    return safe_gold_count

def main():
    width, height = map(int, input().split())
    assert 3 <= width <= 50 and 3 <= height <= 50
    map = [input() for _ in range(height)]
    assert all(len(row) == width for row in map)
    assert all(len(row) == len(set(row)) for row in map)
    assert 'P' in ''.join(map)
    assert all(c in '#P.GT' for row in map for c in row)
    
    print(get_gold_safe(map))

if __name__ == '__main__':
    main()

