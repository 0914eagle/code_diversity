
def is_anti_sudoku(sudoku):
    # Check if the given sudoku is valid
    if len(sudoku) != 9 or any(len(row) != 9 for row in sudoku):
        return False
    
    # Check if the sudoku is correct
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] not in range(1, 10):
                return False
    
    # Check if each row, column, and 3x3 block contains at least two equal elements
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                # Check row
                if sudoku[i].count(sudoku[i][j]) < 2:
                    return False
                # Check column
                if [row[j] for row in sudoku].count(sudoku[i][j]) < 2:
                    return False
                # Check 3x3 block
                start_row = (i // 3) * 3
                start_col = (j // 3) * 3
                block = [sudoku[x][y] for x in range(start_row, start_row + 3) for y in range(start_col, start_col + 3)]
                if block.count(sudoku[i][j]) < 2:
                    return False
    
    return True

def change_sudoku(sudoku):
    # Find an element that can be changed to make the sudoku anti-sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0 and (sudoku[i].count(sudoku[i][j]) < 2 or [row[j] for row in sudoku].count(sudoku[i][j]) < 2 or [sudoku[x][y] for x in range(i // 3 * 3, i // 3 * 3 + 3) for y in range(j // 3 * 3, j // 3 * 3 + 3)].count(sudoku[i][j]) < 2):
                # Change the element and return the new sudoku
                sudoku[i][j] = 0
                return sudoku
    
    # If no element can be changed, return the original sudoku
    return sudoku

def main():
    # Read the input
    t = int(input())
    sudokus = []
    for _ in range(t):
        sudokus.append([list(map(int, input().split())) for _ in range(9)])
    
    # Check if the input is valid
    if any(not is_anti_sudoku(sudoku) for sudoku in sudokus):
        print("Invalid input")
        return
    
    # Change the sudokus to make them anti-sudokus
    anti_sudokus = [change_sudoku(sudoku) for sudoku in sudokus]
    
    # Print the results
    for sudoku in anti_sudokus:
        print("\n".join("".join(str(element) for element in row) for row in sudoku))

if __name__ == '__main__':
    main()

