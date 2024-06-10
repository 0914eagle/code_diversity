
def is_cell_under_attack(x, y, rook_positions):
    # Check if the cell is under attack
    for rook_x, rook_y in rook_positions:
        if x == rook_x or y == rook_y:
            return True
    return False

def get_cells_not_under_attack(n, m, rook_positions):
    # Initialize the board with all cells under attack
    board = [[True] * m for _ in range(n)]

    # Set the cells that are not under attack to False
    for x, y in rook_positions:
        board[x - 1][y - 1] = False

    # Count the number of cells that are not under attack
    cells_not_under_attack = 0
    for row in board:
        for cell in row:
            if not cell:
                cells_not_under_attack += 1

    return cells_not_under_attack

def main():
    n, m = map(int, input().split())
    rook_positions = []
    for _ in range(m):
        x, y = map(int, input().split())
        rook_positions.append((x, y))

    print(get_cells_not_under_attack(n, m, rook_positions))

if __name__ == '__main__':
    main()

