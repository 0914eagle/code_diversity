
def count_unattacked_cells(board_size, rooks_positions):
    # Initialize a board of size (board_size, board_size) with all cells set to 1
    board = [[1] * board_size for _ in range(board_size)]

    # Iterate through the rooks' positions and set the cells under their attack to 0
    for x, y in rooks_positions:
        for i in range(board_size):
            board[x][i] = 0
            board[i][y] = 0

    # Count the number of cells that are not under attack
    unattacked_cells = 0
    for row in board:
        for cell in row:
            if cell == 1:
                unattacked_cells += 1

    return unattacked_cells

def main():
    board_size, num_rooks = map(int, input().split())
    rooks_positions = []
    for _ in range(num_rooks):
        x, y = map(int, input().split())
        rooks_positions.append((x, y))
    print(count_unattacked_cells(board_size, rooks_positions))

if __name__ == '__main__':
    main()

