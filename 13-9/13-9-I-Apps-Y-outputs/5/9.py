
def parse_map(map_string):
    map_list = map_string.split('\n')
    width = len(map_list[0])
    height = len(map_list)
    return width, height, map_list

def find_player(map_list):
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == 'P':
                return i, j
    return None, None

def find_gold(map_list, player_pos):
    gold_count = 0
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == 'G':
                if i == player_pos[0] and j == player_pos[1]:
                    gold_count += 1
    return gold_count

def find_traps(map_list, player_pos):
    trap_count = 0
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == 'T':
                if i == player_pos[0] and j == player_pos[1]:
                    trap_count += 1
    return trap_count

def find_safe_moves(map_list, player_pos):
    safe_moves = []
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] != '#' and map_list[i][j] != 'T':
                safe_moves.append((i, j))
    return safe_moves

def solve(map_string):
    width, height, map_list = parse_map(map_string)
    player_pos = find_player(map_list)
    gold_count = find_gold(map_list, player_pos)
    trap_count = find_traps(map_list, player_pos)
    safe_moves = find_safe_moves(map_list, player_pos)
    return gold_count - trap_count

if __name__ == '__main__':
    map_string = input()
    print(solve(map_string))

