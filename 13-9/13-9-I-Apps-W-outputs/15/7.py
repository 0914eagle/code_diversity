
def get_unattacked_cells(n, m, rooks):
    # Initialize a matrix to keep track of the cells that are not under attack
    unattacked_cells = [[0] * n for _ in range(n)]

    # Loop through each rook and mark the cells that are not under attack
    for i in range(m):
        x, y = rooks[i]
        for j in range(n):
            if j != x:
                unattacked_cells[j][y] += 1
        for k in range(n):
            if k != y:
                unattacked_cells[x][k] += 1

    # Return the number of unattacked cells
    return sum(map(sum, unattacked_cells))

def main():
    n, m = map(int, input().split())
    rooks = []
    for _ in range(m):
        x, y = map(int, input().split())
        rooks.append((x, y))
    print(get_unattacked_cells(n, m, rooks))

if __name__ == '__main__':
    main()

