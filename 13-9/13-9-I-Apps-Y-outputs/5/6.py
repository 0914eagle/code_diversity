
def solve(map):
    # Initialize variables
    gold = 0
    traps = 0
    walls = 0
    player_position = []

    # Parse the map
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == 'P':
                player_position = [i, j]
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
    map = []
    for i in range(int(input())):
        map.append(input())

    # Solve the problem
    result = solve(map)

    # Output the result
    print(result)

if __name__ == '__main__':
    main()

