
def get_gold(map):
    # Initialize variables
    gold = 0
    x, y = 0, 0
    width, height = len(map[0]), len(map)
    traps = []

    # Find the player's starting position
    for i in range(height):
        for j in range(width):
            if map[i][j] == "P":
                x, y = j, i
                break

    # Find all the traps
    for i in range(height):
        for j in range(width):
            if map[i][j] == "T":
                traps.append((j, i))

    # Walk through the map and count the gold
    while x < width and y < height:
        if map[y][x] == "G":
            gold += 1
        if map[y][x] == "T":
            for trap in traps:
                if trap[0] == x and trap[1] == y:
                    return gold
        x += 1
        if x == width:
            x = 0
            y += 1

    return gold

def main():
    map = []
    width, height = map(int, input().split())
    for _ in range(height):
        map.append(input())
    print(get_gold(map))

if __name__ == '__main__':
    main()

