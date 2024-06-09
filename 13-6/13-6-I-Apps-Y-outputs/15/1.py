
def is_valid_sudoku(sudoku):
    # Check if the sudoku is valid
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
    return True

def is_valid_anti_sudoku(sudoku):
    # Check if the sudoku is valid
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
    
    # Check if each row contains at least two equal elements
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if j != k and sudoku[i][j] == sudoku[i][k]:
                    return False
    
    # Check if each column contains at least two equal elements
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if j != k and sudoku[j][i] == sudoku[k][i]:
                    return False
    
    # Check if each 3x3 block contains at least two equal elements
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i+3):
                for l in range(j, j+3):
                    for m in range(i, i+3):
                        for n in range(j, j+3):
                            if k != m and l != n and sudoku[k][l] == sudoku[m][n]:
                                return False
    return True

def solve_anti_sudoku(sudoku):
    # Initialize the number of changes to be made
    num_changes = 9
    
    # Initialize the solution
    solution = [[0] * 9 for _ in range(9)]
    
    # Loop until the solution is found or the number of changes is 0
    while num_changes > 0:
        # Choose a random position to change
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        
        # Check if the chosen position is valid
        if sudoku[i][j] == 0:
            # Change the number at the chosen position to a random number
            solution[i][j] = random.randint(1, 9)
            num_changes -= 1
    
    return solution

def main():
    # Read the input
    t = int(input())
    sudokus = []
    for _ in range(t):
        sudoku = []
        for _ in range(9):
            row = list(map(int, input().split()))
            sudoku.append(row)
        sudokus.append(sudoku)
    
    # Solve the sudokus
    solutions = []
    for sudoku in sudokus:
        solution = solve_anti_sudoku(sudoku)
        solutions.append(solution)
    
    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(" ".join(map(str, row)))

if __name__ == '__main__':
    main()

