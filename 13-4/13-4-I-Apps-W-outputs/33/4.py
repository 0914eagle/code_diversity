
def get_map_size():
    return int(input())

def get_min_bombs_needed(map_size):
    # Implement your solution here
    return 0

def get_bomb_positions(map_size, min_bombs_needed):
    # Implement your solution here
    return []

if __name__ == '__main__':
    map_size = get_map_size()
    min_bombs_needed = get_min_bombs_needed(map_size)
    bomb_positions = get_bomb_positions(map_size, min_bombs_needed)
    print(min_bombs_needed)
    print(" ".join(map(str, bomb_positions)))

