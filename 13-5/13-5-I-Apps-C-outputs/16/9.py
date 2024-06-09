
def is_valid_solution(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if grid[i][j] == grid[i][k] and k != j:
                    return False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if grid[j][i] == grid[k][i] and k != j:
                    return False
    return True

def solve_sudoku(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                for num in range(1, n+1):
                    grid[i][j] = num
                    if is_valid_solution(grid):
                        solve_sudoku(grid)
                    grid[i][j] = 0
                return
    print(grid)

def main():
    n, k = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    for i in range(k):
        grid[i] = list(map(int, input().split()))
    solve_sudoku(grid)

if __name__ == '__main__':
    main()

