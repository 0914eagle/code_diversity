
def find_min_moves(N, tank_positions):
    moves = []
    for i in range(N):
        while tank_positions[i][0] != i + 1 or tank_positions[i][1] != i + 1:
            if tank_positions[i][0] < i + 1:
                tank_positions[i][0] += 1
                moves.append((i + 1, 'D'))
            elif tank_positions[i][0] > i + 1:
                tank_positions[i][0] -= 1
                moves.append((i + 1, 'U'))
            elif tank_positions[i][1] < i + 1:
                tank_positions[i][1] += 1
                moves.append((i + 1, 'R'))
            elif tank_positions[i][1] > i + 1:
                tank_positions[i][1] -= 1
                moves.append((i + 1, 'L'))
    return moves

if __name__ == "__main__":
    N = int(input())
    tank_positions = [list(map(int, input().split())) for _ in range(N)]

    moves = find_min_moves(N, tank_positions)
    print(len(moves))
    for move in moves:
        print(f"{move[0]} {move[1]}")
