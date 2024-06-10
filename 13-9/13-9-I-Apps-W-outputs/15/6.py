
def get_unattacked_cells(n, m, rooks):
    # Initialize a matrix to keep track of the cells that are under attack
    attack_matrix = [[False for _ in range(n)] for _ in range(n)]

    # Iterate through the rooks and mark the cells that are under attack
    for i in range(m):
        x, y = rooks[i]
        attack_matrix[x][y] = True
        for j in range(n):
            attack_matrix[x][j] = True
            attack_matrix[j][y] = True

    # Count the number of cells that are not under attack
    unattacked_cells = 0
    for i in range(n):
        for j in range(n):
            if not attack_matrix[i][j]:
                unattacked_cells += 1

    return unattacked_cells

def main():
    n, m = map(int, input().split())
    rooks = []
    for i in range(m):
        x, y = map(int, input().split())
        rooks.append((x, y))
    print(get_unattacked_cells(n, m, rooks))

if __name__ == '__main__':
    main()

