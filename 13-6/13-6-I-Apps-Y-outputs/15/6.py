
def solve_sudoku(sudoku):
    # Function to check if a given number is valid in a given row, column and 3x3 box
    def is_valid(row, col, num):
        for i in range(9):
            if sudoku[row][i] == num or sudoku[i][col] == num:
                return False
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if sudoku[i][j] == num:
                    return False
        return True

    # Function to solve the sudoku puzzle
    def solve(sudoku):
        # Find the next empty cell (i, j) with the minimum number of possible values (min_val)
        min_val = 10
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0 and min_val > 9 - len(set(sudoku[i])) - len(set([sudoku[j][k] for k in range(9)])):
                    min_val = 9 - len(set(sudoku[i])) - len(set([sudoku[j][k] for k in range(9)]))
                    row, col = i, j

        # If there are no empty cells, the puzzle is solved
        if min_val == 10:
            return True

        # Iterate through the possible values (1-9) and recursively call the solve function
        for num in range(1, 10):
            if is_valid(row, col, num):
                sudoku[row][col] = num
                if solve(sudoku):
                    return True
                sudoku[row][col] = 0

        # If the puzzle cannot be solved, return False
        return False

    # Function to convert the sudoku puzzle to an anti-sudoku
    def to_anti_sudoku(sudoku):
        # Initialize the anti-sudoku with the given sudoku puzzle
        anti_sudoku = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                anti_sudoku[i][j] = sudoku[i][j]

        # Change at most 9 elements of the anti-sudoku to make it anti-sudoku
        for _ in range(9):
            i, j = random.randint(0, 8), random.randint(0, 8)
            if anti_sudoku[i][j] != 0:
                anti_sudoku[i][j] = 0
            else:
                anti_sudoku[i][j] = random.randint(1, 9)

        return anti_sudoku

    # Solve the sudoku puzzle
    if solve(sudoku):
        # Convert the solved sudoku puzzle to an anti-sudoku
        anti_sudoku = to_anti_sudoku(sudoku)
        return anti_sudoku
    else:
        return []

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        sudoku = [[int(i) for i in input().split()] for _ in range(9)]
        anti_sudoku = solve_sudoku(sudoku)
        if anti_sudoku:
            for row in anti_sudoku:
                print(*row)
        else:
            print(-1)

