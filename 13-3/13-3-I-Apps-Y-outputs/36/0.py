
def get_gold(map):
    # Initialize variables
    gold = 0
    traps = 0
    walls = 0
    player_position = None
    
    # Parse the map
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == 'P':
                player_position = (i, j)
            elif cell == 'G':
                gold += 1
            elif cell == 'T':
                traps += 1
            elif cell == '#':
                walls += 1
    
    # Calculate the maximum gold the player can get
    max_gold = gold - traps
    
    # Return the maximum gold
    return max_gold

def main():
    # Read the map from stdin
    map = [input() for _ in range(int(input()))]
    
    # Get the maximum gold the player can get
    max_gold = get_gold(map)
    
    # Print the result
    print(max_gold)

if __name__ == '__main__':
    main()

