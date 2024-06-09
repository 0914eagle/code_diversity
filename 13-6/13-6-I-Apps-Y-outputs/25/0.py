
def read_grid(N, M):
    grid = []
    for _ in range(N):
        grid.append(input())
    return grid

def count_moves(grid):
    moves = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '$':
                moves += 1
    return moves

def main():
    N, M = map(int, input().split())
    grid = read_grid(N, M)
    print(count_moves(grid))

if __name__ == '__main__':
    main()

