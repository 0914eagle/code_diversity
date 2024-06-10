
def get_non_attacked_cells(n, rooks):
    # Initialize a grid to keep track of the cells that are not under attack
    grid = [[0] * n for _ in range(n)]

    # Iterate over the rooks and mark the cells that are not under attack
    for i, (x, y) in enumerate(rooks):
        # Mark the current cell as not under attack
        grid[x][y] = 1

        # Mark the cells in the same row as not under attack
        for j in range(n):
            if grid[x][j] == 0:
                grid[x][j] = 1

        # Mark the cells in the same column as not under attack
        for j in range(n):
            if grid[j][y] == 0:
                grid[j][y] = 1

    # Count the number of cells that are not under attack
    non_attacked_cells = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                non_attacked_cells += 1

    return non_attacked_cells

def main():
    n, m = map(int, input().split())
    rooks = []
    for _ in range(m):
        x, y = map(int, input().split())
        rooks.append((x, y))
    print(get_non_attacked_cells(n, rooks))

if __name__ == '__main__':
    main()

