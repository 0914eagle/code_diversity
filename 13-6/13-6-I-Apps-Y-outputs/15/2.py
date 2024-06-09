
def get_anti_sudoku(sudoku):
    # Convert the sudoku to a 2D array for easier manipulation
    sudoku = [[int(sudoku[i * 9 + j]) for j in range(9)] for i in range(9)]
    
    # Find the row, column, and block with the most duplicates
    row_duplicates = []
    col_duplicates = []
    block_duplicates = []
    for i in range(9):
        row = sudoku[i]
        col = [row[j] for j in range(9)]
        block = [sudoku[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] for j in range(9)]
        row_duplicates.append(len(set(row)) != 9)
        col_duplicates.append(len(set(col)) != 9)
        block_duplicates.append(len(set(block)) != 9)
    row_index = row_duplicates.index(True)
    col_index = col_duplicates.index(True)
    block_index = block_duplicates.index(True)
    
    # Find the element to change
    element_to_change = None
    for i in range(9):
        if sudoku[row_index][i] != 0 and sudoku[row_index][i] != sudoku[col_index][i] and sudoku[row_index][i] != sudoku[block_index][i]:
            element_to_change = (row_index, i)
            break
    if element_to_change is None:
        return None
    
    # Change the element and return the anti-sudoku
    sudoku[element_to_change[0]][element_to_change[1]] = 0
    return "".join([str(sudoku[i][j]) for i in range(9) for j in range(9)])

def main():
    t = int(input())
    for _ in range(t):
        sudoku = input()
        anti_sudoku = get_anti_sudoku(sudoku)
        print(anti_sudoku)

if __name__ == '__main__':
    main()

