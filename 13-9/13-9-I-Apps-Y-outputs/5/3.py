
def parse_input(input_string):
    
    width, height = map(int, input_string.splitlines()[0].split())
    map = []
    for i in range(1, height+1):
        map.append(list(input_string.splitlines()[i]))
    return map

def get_gold(map):
    
    gold = 0
    for row in map:
        for col in row:
            if col == "G":
                gold += 1
    return gold

def get_traps(map):
    
    traps = 0
    for row in map:
        for col in row:
            if col == "T":
                traps += 1
    return traps

def get_safe_moves(map):
    
    safe_moves = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == ".":
                safe_moves += 1
    return safe_moves

def main():
    map = parse_input(input())
    gold = get_gold(map)
    traps = get_traps(map)
    safe_moves = get_safe_moves(map)
    print(gold - traps * safe_moves)

if __name__ == '__main__':
    main()

