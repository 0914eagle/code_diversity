
def is_sudoku_solved(grid):
    # Check if the grid is valid
    if len(grid) != 9 or len(grid[0]) != 9:
        return False
    
    # Check if each row, column, and block contains each number only once
    for i in range(9):
        for j in range(9):
            if grid[i][j] not in range(1, 10):
                return False
            for k in range(9):
                if grid[i][j] == grid[i][k] and j != k:
                    return False
                if grid[i][j] == grid[k][j] and i != k:
                    return False
            for row in (0, 3, 6):
                for col in (0, 3, 6):
                    if grid[i][j] == grid[row + i % 3][col + j % 3] and (row + i % 3 != i or col + j % 3 != j):
                        return False
    
    return True

def is_sudoku_anti(grid):
    # Check if the grid is valid
    if len(grid) != 9 or len(grid[0]) != 9:
        return False
    
    # Check if each row, column, and block contains at least two equal elements
    for i in range(9):
        for j in range(9):
            count = 0
            for k in range(9):
                if grid[i][j] == grid[i][k] and j != k:
                    count += 1
            if count < 2:
                return False
            count = 0
            for k in range(9):
                if grid[i][j] == grid[k][j] and i != k:
                    count += 1
            if count < 2:
                return False
            for row in (0, 3, 6):
                for col in (0, 3, 6):
                    count = 0
                    if grid[i][j] == grid[row + i % 3][col + j % 3] and (row + i % 3 != i or col + j % 3 != j):
                        count += 1
            if count < 2:
                return False
    
    return True

def solve_sudoku(grid):
    # Check if the grid is already solved
    if is_sudoku_solved(grid):
        return grid
    
    # Find the first empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                break
        else:
            continue
        break
    
    # Try all possible values for the empty cell
    for value in range(1, 10):
        grid[i][j] = value
        if is_sudoku_anti(grid):
            return grid
    
    # If no value works, backtrack
    grid[i][j] = 0
    return solve_sudoku(grid)

def main():
    t = int(input())
    for _ in range(t):
        grid = []
        for _ in range(9):
            grid.append(list(map(int, input().split())))
        print(solve_sudoku(grid))

if __name__ == '__main__':
    main()

