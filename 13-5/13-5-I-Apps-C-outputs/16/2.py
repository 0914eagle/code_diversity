
def is_valid_solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0 and grid[i][j] != i + 1:
                return False
    return True

def solve_superdoku(n, k, grid):
    for i in range(k, n):
        for j in range(n):
            if grid[i][j] == 0:
                for num in range(1, n + 1):
                    grid[i][j] = num
                    if is_valid_solution(grid):
                        if solve_superdoku(n, k, grid):
                            return True
                    grid[i][j] = 0
    return is_valid_solution(grid)

def main():
    n, k = map(int, input().split())
    grid = []
    for i in range(k):
        grid.append(list(map(int, input().split())))
    if solve_superdoku(n, k, grid):
        for i in range(k):
            print(*grid[i])

if __name__ == '__main__':
    main()

