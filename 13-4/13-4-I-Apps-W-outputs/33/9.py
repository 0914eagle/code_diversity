
def get_map_size():
    return int(input())

def get_tank_positions(map_size):
    return [int(i) for i in input().split()]

def get_min_bombs(map_size, tank_positions):
    bomb_positions = set()
    for tank_position in tank_positions:
        bomb_positions.add(tank_position)
        for neighbor in get_neighbors(map_size, tank_position):
            if neighbor not in bomb_positions:
                bomb_positions.add(neighbor)
    return len(bomb_positions)

def get_neighbors(map_size, position):
    neighbors = []
    if position > 1:
        neighbors.append(position - 1)
    if position < map_size:
        neighbors.append(position + 1)
    return neighbors

def main():
    map_size = get_map_size()
    tank_positions = get_tank_positions(map_size)
    min_bombs = get_min_bombs(map_size, tank_positions)
    print(min_bombs)
    print(*tank_positions)

if __name__ == '__main__':
    main()

