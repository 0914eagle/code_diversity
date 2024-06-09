
def is_valid_sudoku(grid):
    # Check rows
    for i in range(len(grid)):
        row = grid[i]
        if len(set(row)) != len(row):
            return False

    # Check columns
    for j in range(len(grid[0])):
        column = [row[j] for row in grid]
        if len(set(column)) != len(column):
            return False

    # Check boxes
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            box = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(box)) != len(box):
                return False

    return True

def solve_superdoku(grid, k):
    # Check if the first k rows are valid
    for i in range(k):
        if not is_valid_sudoku(grid[i]):
            return False

    # Check if the remaining rows are valid
    for i in range(k, len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                continue
            for num in range(1, len(grid) + 1):
                grid[i][j] = num
                if is_valid_sudoku(grid):
                    if solve_superdoku(grid, k):
                        return True
                grid[i][j] = 0
            return False

    return True

def main():
    n, k = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    if solve_superdoku(grid, k):
        for row in grid:
            print(*row)
    else:
        print("No solution")

if __name__ == "__main__":
    main()

