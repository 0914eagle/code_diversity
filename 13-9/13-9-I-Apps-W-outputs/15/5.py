
def count_unattacked_cells(n, m, rooks):
    # Initialize a 2D array to store the state of the board
    board = [[0] * n for _ in range(n)]

    # Iterate over the rooks and mark their positions on the board
    for x, y in rooks:
        board[x - 1][y - 1] = 1

    # Count the number of unattacked cells
    unattacked_cells = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                unattacked_cells += 1

    return unattacked_cells

def main():
    n, m = map(int, input().split())
    rooks = []
    for _ in range(m):
        x, y = map(int, input().split())
        rooks.append((x, y))
    print(count_unattacked_cells(n, m, rooks))

if __name__ == '__main__':
    main()

