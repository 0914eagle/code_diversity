_tank(current_pos, target_pos):
    moves = []
    while current_pos != target_pos:
        if current_pos[0] < target_pos[0]:
            moves.append('D')
            current_pos = (current_pos[0] + 1, current_pos[1])
        elif current_pos[0] > target_pos[0]:
            moves.append('U')
            current_pos = (current_pos[0] - 1, current_pos[1])
        if current_pos[1] < target_pos[1]:
            moves.append('R')
            current_pos = (current_pos[0], current_pos[1] + 1)
        elif current_pos[1] > target_pos[1]:
            moves.append('L')
            current_pos = (current_pos[0], current_pos[1] - 1)
    return moves

def rearrange_tanks(N, tank_positions):
    moves_list = []
    for i in range(N):
        target_pos = (i + 1, tank_positions[i][1])
        moves_list.extend(move_tank(tank_positions[i], target_pos))
        moves_list.append(f"{i + 1} D")
    return moves_list

def min_moves_to_rearrange(N, tank_positions):
    moves_list = rearrange_tanks(N, tank_positions)
    print(len(moves_list))
    for move in moves_list:
        print(move)

if __name__ == "__main__":
    N = int(input())
    tank_positions = [tuple(map(int, input().split())) for _ in range(N)]
    min_moves_to_rearrange(N, tank_positions)
