ulate_distance(tank_pos, target_pos):
    return abs(tank_pos[0] - target_pos[0]) + abs(tank_pos[1] - target_pos[1])

def move_tank(tank, direction):
    if direction == 'L':
        return tank[0], tank[1] - 1
    elif direction == 'R':
        return tank[0], tank[1] + 1
    elif direction == 'U':
        return tank[0] - 1, tank[1]
    elif direction == 'D':
        return tank[0] + 1, tank[1]

def rearrange_tanks(N, initial_positions):
    moves = []
    tanks = initial_positions.copy()
    for i in range(N):
        target_pos = (i + 1, i + 1)
        max_distance = float('-inf')
        tank_to_move = None
        for j, tank in enumerate(tanks):
            distance = calculate_distance(tank, target_pos)
            if distance > max_distance:
                max_distance = distance
                tank_to_move = j
        while tanks[tank_to_move] != target_pos:
            if tanks[tank_to_move][0] < target_pos[0]:
                direction = 'D'
            elif tanks[tank_to_move][0] > target_pos[0]:
                direction = 'U'
            elif tanks[tank_to_move][1] < target_pos[1]:
                direction = 'R'
            else:
                direction = 'L'
            tanks[tank_to_move] = move_tank(tanks[tank_to_move], direction)
            moves.append((tank_to_move + 1, direction))
    return moves

def main():
    N = int(input())
    initial_positions = []
    for _ in range(N):
        R, C = map(int, input().split())
        initial_positions.append((R, C))

    moves = rearrange_tanks(N, initial_positions)
    print(len(moves))
    for move in moves:
        print(f"{move[0]} {move[1]}")

if __name__ == "__main__":
    main()
