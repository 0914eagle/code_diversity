
def solve_sudoku(sudoku):
    # Check if the given sudoku is valid
    if not is_valid_sudoku(sudoku):
        return None
    
    # Initialize the number of changes to be made
    num_changes = 0
    
    # Loop through each row, column, and block
    for i in range(9):
        for j in range(9):
            # If the current cell is empty, find a valid number to fill it with
            if sudoku[i][j] == 0:
                num_changes += 1
                sudoku[i][j] = find_valid_number(sudoku, i, j)
    
    # If the number of changes is less than or equal to 9, return the modified sudoku
    if num_changes <= 9:
        return sudoku
    
    # If the number of changes is greater than 9, return None
    return None

def is_valid_sudoku(sudoku):
    # Check if each row, column, and block contains each number only once
    for i in range(9):
        for j in range(9):
            if not is_valid_row(sudoku, i) or not is_valid_column(sudoku, j) or not is_valid_block(sudoku, i, j):
                return False
    
    return True

def is_valid_row(sudoku, row):
    numbers = set()
    for i in range(9):
        if sudoku[row][i] != 0 and sudoku[row][i] in numbers:
            return False
        numbers.add(sudoku[row][i])
    return True

def is_valid_column(sudoku, column):
    numbers = set()
    for i in range(9):
        if sudoku[i][column] != 0 and sudoku[i][column] in numbers:
            return False
        numbers.add(sudoku[i][column])
    return True

def is_valid_block(sudoku, row, column):
    numbers = set()
    for i in range(3):
        for j in range(3):
            cell = (row // 3) * 3 + i
            cell = (column // 3) * 3 + j
            if sudoku[cell][cell] != 0 and sudoku[cell][cell] in numbers:
                return False
            numbers.add(sudoku[cell][cell])
    return True

def find_valid_number(sudoku, row, column):
    # Find a valid number that is not already in the row, column, or block
    for number in range(1, 10):
        if not is_valid_number(sudoku, row, column, number):
            continue
        return number
    
    # If no valid number is found, return 0
    return 0

def is_valid_number(sudoku, row, column, number):
    # Check if the number is not already in the row, column, or block
    for i in range(9):
        if sudoku[row][i] == number or sudoku[i][column] == number or sudoku[(row // 3) * 3 + i // 3][(column // 3) * 3 + i % 3] == number:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        sudoku = []
        for _ in range(9):
            sudoku.append(list(map(int, input().split())))
        result = solve_sudoku(sudoku)
        if result is None:
            print("No solution")
        else:
            for row in result:
                print(" ".join(map(str, row)))

