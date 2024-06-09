
def is_valid_solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0 and grid[i][j] != i + 1:
                return False
    return True

def solve_sudoku(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                for num in range(1, len(grid) + 1):
                    grid[i][j] = num
                    if is_valid_solution(grid):
                        if solve_sudoku(grid):
                            return True
                    grid[i][j] = 0
    return False

def solve_superdoku(grid, k):
    for i in range(k):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                for num in range(1, len(grid) + 1):
                    grid[i][j] = num
                    if is_valid_solution(grid):
                        if solve_sudoku(grid):
                            return True
                    grid[i][j] = 0
    return False

def main():
    n, k = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    for i in range(k):
        grid[i] = list(map(int, input().split()))
    if solve_superdoku(grid, k):
        print("yes")
        for row in grid:
            print(*row)
    else:
        print("no")

if __name__ == '__main__':
    main()

