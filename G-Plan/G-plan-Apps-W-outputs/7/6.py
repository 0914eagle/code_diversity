
def move_tank(current_pos, target_pos):
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
    for i, (r, c) in enumerate(tank_positions, start=1):
        target_r, target_c = (i, i)
        moves = move_tank((r, c), (target_r, target_c))
        moves_list.extend([(i, move) for move in moves])
    return moves_list

if __name__ == "__main__":
    N = int(input())
    tank_positions = [tuple(map(int, input().split())) for _ in range(N)]
    
    moves = rearrange_tanks(N, tank_positions)
    
    print(len(moves))
    for tank, direction in moves:
        print(tank, direction)
