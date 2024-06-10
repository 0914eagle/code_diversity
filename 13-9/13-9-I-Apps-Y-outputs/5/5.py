
def get_gold_safe(map):
    # Initialize variables
    gold_count = 0
    traps_nearby = 0
    player_position = None
    # Parse the map
    for i, row in enumerate(map):
        for j, symbol in enumerate(row):
            if symbol == "P":
                player_position = (i, j)
            elif symbol == "G":
                gold_count += 1
            elif symbol == "T":
                traps_nearby += 1
    # Move the player to the left and right of the trap, and count the gold
    for i in range(player_position[1] - 1, player_position[1] + 2):
        if i >= 0 and i < len(map[0]) and map[player_position[0]][i] == "G":
            gold_count += 1
    # Move the player up and down of the trap, and count the gold
    for i in range(player_position[0] - 1, player_position[0] + 2):
        if i >= 0 and i < len(map) and map[i][player_position[1]] == "G":
            gold_count += 1
    # Return the number of gold the player can get safely
    return gold_count - traps_nearby

def main():
    # Read the map from stdin
    width, height = map(int, input().split())
    map = []
    for i in range(height):
        map.append(input())
    # Call the get_gold_safe function and print the result
    print(get_gold_safe(map))

if __name__ == '__main__':
    main()

