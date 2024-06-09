
def is_valid_sudoku(sudoku):
    # Check if the sudoku is valid
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in range(1, 10):
                return False
    return True

def is_valid_anti_sudoku(sudoku):
    # Check if the sudoku is valid
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in range(1, 10):
                return False
    
    # Check if each row contains at least two equal elements
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                if sudoku[i][j] == sudoku[i][k]:
                    return False
    
    # Check if each column contains at least two equal elements
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                if sudoku[j][i] == sudoku[k][i]:
                    return False
    
    # Check if each 3x3 block contains at least two equal elements
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i+3):
                for l in range(j, j+3):
                    for m in range(k, i+3):
                        for n in range(l, j+3):
                            if sudoku[k][l] == sudoku[m][n]:
                                return False
    return True

def solve_anti_sudoku(sudoku):
    # Initialize the solution
    solution = [[0 for _ in range(9)] for _ in range(9)]
    
    # Iterate through the rows
    for i in range(9):
        # Iterate through the columns
        for j in range(9):
            # If the element is not zero, set the solution to that value
            if sudoku[i][j] != 0:
                solution[i][j] = sudoku[i][j]
    
    # Iterate through the rows
    for i in range(9):
        # Iterate through the columns
        for j in range(9):
            # If the element is zero, set the solution to any value that is not in the row, column, or block
            if solution[i][j] == 0:
                for k in range(1, 10):
                    if k not in sudoku[i] and k not in [sudoku[j][c] for c in range(9)] and k not in [sudoku[r][j] for r in range(9)]:
                        solution[i][j] = k
                        break
    
    return solution

def main():
    t = int(input())
    for _ in range(t):
        sudoku = [[int(input()) for _ in range(9)] for _ in range(9)]
        if is_valid_sudoku(sudoku):
            solution = solve_anti_sudoku(sudoku)
            if is_valid_anti_sudoku(solution):
                for i in range(9):
                    print(*solution[i])
            else:
                print("No solution exists")
        else:
            print("No solution exists")

if __name__ == '__main__':
    main()

