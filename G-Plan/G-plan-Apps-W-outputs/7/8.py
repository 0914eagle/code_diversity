_tank(board, tank, target_row, target_col):
    moves = []
    current_row, current_col = tank
    while current_row != target_row:
        if current_row < target_row:
            current_row += 1
            moves.append(f"{board[current_row][current_col]} D")
        else:
            current_row -= 1
            moves.append(f"{board[current_row][current_col]} U")
    while current_col != target_col:
        if current_col < target_col:
            current_col += 1
            moves.append(f"{board[current_row][current_col]} R")
        else:
            current_col -= 1
            moves.append(f"{board[current_row][current_col]} L")
    return moves


def rearrange_tanks(N, initial_positions):
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i, (row, col) in enumerate(initial_positions, start=1):
        board[row - 1][col - 1] = i

    moves = []
    for i, (row, col) in enumerate(initial_positions, start=1):
        target_row, target_col = i, i
        if board[target_row - 1][target_col - 1] == i:
            continue
        moves += move_tank(board, (row - 1, col - 1), target_row - 1, target_col - 1)

    return moves


if __name__ == "__main__":
    N = int(input())
    initial_positions = [tuple(map(int, input().split())) for _ in range(N)]

    moves = rearrange_tanks(N, initial_positions)
    print(len(moves))
    for move in moves:
        print(move)
