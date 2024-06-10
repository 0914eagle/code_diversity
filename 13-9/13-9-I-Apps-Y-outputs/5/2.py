
def get_gold(map):
    # Initialize variables
    gold_count = 0
    traps_near = 0
    player_x = 0
    player_y = 0

    # Find the player's starting position
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == 'P':
                player_x = x
                player_y = y
                break

    # Iterate through the map
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            # Check if the current cell is a gold piece
            if char == 'G':
                gold_count += 1

            # Check if the current cell is a trap
            if char == 'T':
                traps_near += 1

            # Check if the current cell is a wall
            if char == '#':
                continue

            # Check if the current cell is a safe position
            if traps_near == 0:
                # Calculate the distance from the player to the current cell
                dist = abs(player_x - x) + abs(player_y - y)

                # If the distance is 1, the current cell is safe and the player can move there
                if dist == 1:
                    gold_count += 1

    return gold_count

def main():
    width, height = map(int, input().split())
    map = [input() for _ in range(height)]
    print(get_gold(map))

if __name__ == '__main__':
    main()

