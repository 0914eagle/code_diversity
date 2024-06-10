
def count_unattacked_cells(board_size, rook_positions):
    # Initialize a matrix to keep track of the cells that are under attack
    attacked_cells = [[False for _ in range(board_size)] for _ in range(board_size)]

    # Loop through all the rook positions and mark the cells that are under attack
    for x, y in rook_positions:
        for i in range(board_size):
            attacked_cells[x][i] = True
            attacked_cells[i][y] = True

    # Count the number of unattacked cells
    unattacked_cells = 0
    for i in range(board_size):
        for j in range(board_size):
            if not attacked_cells[i][j]:
                unattacked_cells += 1

    return unattacked_cells

def main():
    board_size, num_rooks = map(int, input().split())
    rook_positions = []
    for _ in range(num_rooks):
        x, y = map(int, input().split())
        rook_positions.append((x, y))
    print(count_unattacked_cells(board_size, rook_positions))

if __name__ == '__main__':
    main()

