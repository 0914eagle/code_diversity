
import sys
input = sys.stdin.read()

def get_map_size(input_map):
    return len(input_map), len(input_map[0])

def get_starting_position(input_map):
    for row in range(len(input_map)):
        for col in range(len(input_map[0])):
            if input_map[row][col] == "S":
                return row, col

def get_gold_position(input_map):
    for row in range(len(input_map)):
        for col in range(len(input_map[0])):
            if input_map[row][col] == "G":
                return row, col

def get_moves(row, col, input_map):
    moves = []
    if row > 0 and input_map[row-1][col] != "#":
        moves.append((row-1, col))
    if row < len(input_map)-1 and input_map[row+1][col] != "#":
        moves.append((row+1, col))
    if col > 0 and input_map[row][col-1] != "#":
        moves.append((row, col-1))
    if col < len(input_map[0])-1 and input_map[row][col+1] != "#":
        moves.append((row, col+1))
    return moves

def get_min_days(input_map, starting_position, gold_position, stamina):
    queue = [(starting_position, 0, stamina)]
    visited = set()
    while queue:
        current_position, days, current_stamina = queue.pop(0)
        if current_position == gold_position:
            return days
        if current_position in visited:
            continue
        visited.add(current_position)
        moves = get_moves(*current_position, input_map)
        for move in moves:
            new_stamina = current_stamina - 1
            if new_stamina <= 0:
                new_stamina = stamina
            queue.append((move, days+1, new_stamina))
    return -1

def main():
    input_map = [list(line) for line in input.split("\n") if line.strip()]
    starting_position = get_starting_position(input_map)
    gold_position = get_gold_position(input_map)
    stamina = int(input())
    print(get_min_days(input_map, starting_position, gold_position, stamina))

if __name__ == "__main__":
    main()

