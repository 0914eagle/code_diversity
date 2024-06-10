_tank(current_row, current_col, target_row, target_col):
    moves = []
    while current_row != target_row:
        if current_row < target_row:
            current_row += 1
            moves.append("D")
        else:
            current_row -= 1
            moves.append("U")
    while current_col != target_col:
        if current_col < target_col:
            current_col += 1
            moves.append("R")
        else:
            current_col -= 1
            moves.append("L")
    return moves

def rearrange_tanks(N, tanks):
    moves_list = []
    for i in range(N):
        current_row, current_col = tanks[i]
        target_row, target_col = i + 1, i + 1
        if current_row != target_row or current_col != target_col:
            moves = move_tank(current_row, current_col, target_row, target_col)
            moves_list.extend([(i + 1, move) for move in moves])
    return moves_list

def main():
    N = int(input())
    tanks = [list(map(int, input().split())) for _ in range(N)]
    moves = rearrange_tanks(N, tanks)
    print(len(moves))
    for tank, direction in moves:
        print(tank, direction)

if __name__ == "__main__":
    main()
