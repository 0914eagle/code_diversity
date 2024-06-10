
def get_input():
    W, H = map(int, input().split())
    assert 3 <= W <= 50 and 3 <= H <= 50
    map = []
    for _ in range(H):
        map.append(input())
    return W, H, map

def get_safe_gold(W, H, map):
    # Initialize variables
    gold = 0
    x, y = 0, 0
    traps = set()
    walls = set()

    # Iterate through the map
    for i in range(H):
        for j in range(W):
            char = map[i][j]
            if char == 'P':
                x, y = j, i
            elif char == 'G':
                gold += 1
            elif char == 'T':
                traps.add((j, i))
            elif char == '#':
                walls.add((j, i))

    # Calculate the safe gold
    for trap in traps:
        if trap[0] == x or trap[1] == y:
            gold -= 1
        elif trap[0] in [x-1, x+1] and trap[1] in [y-1, y+1]:
            gold -= 1
        elif trap[0] in [x-1, x+1] and trap[1] in [y, y+2]:
            gold -= 1
        elif trap[0] in [x, x+2] and trap[1] in [y-1, y+1]:
            gold -= 1
        elif trap[0] in [x, x+2] and trap[1] in [y, y+2]:
            gold -= 1

    return gold

def main():
    W, H, map = get_input()
    print(get_safe_gold(W, H, map))

if __name__ == '__main__':
    main()

