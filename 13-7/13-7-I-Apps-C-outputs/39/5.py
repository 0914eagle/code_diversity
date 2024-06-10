
def get_map_size(map_string):
    return len(map_string), len(map_string[0])

def get_starting_position(map_string):
    for i, row in enumerate(map_string):
        for j, char in enumerate(row):
            if char == "S":
                return i, j

def get_treasure_position(map_string):
    for i, row in enumerate(map_string):
        for j, char in enumerate(row):
            if char == "G":
                return i, j

def get_movement_cost(map_string, current_position, new_position):
    cost = 0
    if map_string[new_position[0]][new_position[1]] == ".":
        cost = 1
    elif map_string[new_position[0]][new_position[1]] == "F":
        cost = 2
    elif map_string[new_position[0]][new_position[1]] == "M":
        cost = 3
    return cost

def is_valid_position(map_string, position):
    return position[0] >= 0 and position[1] >= 0 and position[0] < len(map_string) and position[1] < len(map_string[0])

def is_treasure_reached(map_string, current_position, treasure_position):
    return current_position == treasure_position

def bfs(map_string, starting_position, treasure_position, stamina):
    queue = [(starting_position, stamina)]
    visited = set()
    while queue:
        current_position, current_stamina = queue.pop(0)
        if is_treasure_reached(map_string, current_position, treasure_position):
            return current_stamina
        if current_stamina <= 0:
            continue
        for new_position in [(current_position[0]-1, current_position[1]), (current_position[0]+1, current_position[1]), (current_position[0], current_position[1]-1), (current_position[0], current_position[1]+1)]:
            if is_valid_position(map_string, new_position) and new_position not in visited:
                visited.add(new_position)
                queue.append((new_position, current_stamina - get_movement_cost(map_string, current_position, new_position)))
    return -1

def solve(map_string, stamina):
    map_size = get_map_size(map_string)
    starting_position = get_starting_position(map_string)
    treasure_position = get_treasure_position(map_string)
    return bfs(map_string, starting_position, treasure_position, stamina)

if __name__ == '__main__':
    map_string = input()
    stamina = int(input())
    print(solve(map_string, stamina))

