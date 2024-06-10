
def get_unattacked_cells(board_size, rooks):
    # Initialize a matrix to keep track of the cells that are under attack
    attack_matrix = [[False for _ in range(board_size)] for _ in range(board_size)]

    # Mark the cells that are under attack by the rooks
    for rook in rooks:
        row, col = rook
        for i in range(board_size):
            attack_matrix[i][col] = True
            attack_matrix[row][i] = True

    # Count the number of cells that are not under attack
    unattacked_cells = 0
    for i in range(board_size):
        for j in range(board_size):
            if not attack_matrix[i][j]:
                unattacked_cells += 1

    return unattacked_cells

def main():
    board_size, num_rooks = map(int, input().split())
    rooks = []
    for _ in range(num_rooks):
        rook = list(map(int, input().split()))
        rooks.append(rook)
    unattacked_cells = get_unattacked_cells(board_size, rooks)
    print(unattacked_cells)

if __name__ == '__main__':
    main()

