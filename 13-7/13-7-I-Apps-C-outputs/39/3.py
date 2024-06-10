
def read_map(grid):
    N, M, K = map(int, input().split())
    grid = [input() for _ in range(N)]
    return N, M, K, grid

def find_treasure(N, M, K, grid):
    days = 0
    stamina = K
    row, col = 0, 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                row, col = i, j
                break
        if row != 0 and col != 0:
            break
    while True:
        if grid[row][col] == 'G':
            break
        if grid[row][col] == '.':
            stamina -= 1
        elif grid[row][col] == 'F':
            stamina -= 2
        elif grid[row][col] == 'M':
            stamina -= 3
        elif grid[row][col] == '#':
            return -1
        if stamina == 0:
            days += 1
            stamina = K
        if grid[row][col] == 'G':
            break
        if grid[row][col] == '.':
            row -= 1
        elif grid[row][col] == 'F':
            col += 1
        elif grid[row][col] == 'M':
            row += 1
        elif grid[row][col] == '#':
            return -1
    return days

def main():
    grid = []
    N, M, K, grid = read_map(grid)
    print(find_treasure(N, M, K, grid))

if __name__ == '__main__':
    main()

