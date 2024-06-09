
def is_valid_sudoku(grid):
    # Check rows
    for i in range(len(grid)):
        row = grid[i]
        if len(set(row)) != len(row):
            return False

    # Check columns
    for i in range(len(grid[0])):
        column = [row[i] for row in grid]
        if len(set(column)) != len(column):
            return False

    # Check boxes
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            box = [grid[x][y] for x in range(i * 3, i * 3 + 3) for y in range(j * 3, j * 3 + 3)]
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
            if grid[i][j] != 0 and grid[i][j] not in grid[i]:
                return False

    # Check if the grid is valid
    if not is_valid_sudoku(grid):
        return False

    # If the grid is valid, return it
    return grid

def main():
    n, k = map(int, input().split())
    grid = []
    for i in range(k):
        grid.append(list(map(int, input().split())))
    for i in range(k, n):
        grid.append([0] * n)
    solution = solve_superdoku(grid, k)
    if solution:
        print("yes")
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("no")

if __name__ == "__main__":
    main()

