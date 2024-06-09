
def get_anti_sudoku(sudoku):
    # Initialize a dictionary to store the number of occurrences of each number in each row, column, and block
    row_counts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    col_counts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    block_counts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    
    # Populate the dictionary with the initial counts
    for i in range(9):
        for j in range(9):
            num = int(sudoku[i][j])
            row_counts[i][num] = row_counts[i].get(num, 0) + 1
            col_counts[j][num] = col_counts[j].get(num, 0) + 1
            block_counts[i // 3 * 3 + j // 3][num] = block_counts[i // 3 * 3 + j // 3].get(num, 0) + 1
    
    # Find the row, column, and block with the least number of occurrences of each number
    least_row = [0] * 9
    least_col = [0] * 9
    least_block = [0] * 9
    for i in range(9):
        for j in range(1, 10):
            if row_counts[i].get(j, 0) < row_counts[least_row[i]][j]:
                least_row[i] = j
            if col_counts[i].get(j, 0) < col_counts[least_col[i]][j]:
                least_col[i] = j
            if block_counts[i].get(j, 0) < block_counts[least_block[i]][j]:
                least_block[i] = j
    
    # Change the numbers in the row, column, and block with the least number of occurrences to any other number
    for i in range(9):
        for j in range(1, 10):
            if row_counts[i][j] == 0 and least_row[i] == j:
                row_counts[i][j] = 1
                sudoku[i] = [str(j) if k != i else str(least_row[i]) for k, v in enumerate(sudoku[i])]
            if col_counts[i][j] == 0 and least_col[i] == j:
                col_counts[i][j] = 1
                for k in range(9):
                    if sudoku[k][i] == str(j):
                        sudoku[k][i] = str(least_col[i])
            if block_counts[i][j] == 0 and least_block[i] == j:
                block_counts[i][j] = 1
                for k in range(i // 3 * 3, i // 3 * 3 + 3):
                    for l in range(i % 3 * 3, i % 3 * 3 + 3):
                        if sudoku[k][l] == str(j):
                            sudoku[k][l] = str(least_block[i])
    
    return sudoku

def main():
    t = int(input())
    for _ in range(t):
        sudoku = [input() for _ in range(9)]
        anti_sudoku = get_anti_sudoku(sudoku)
        print('\n'.join(anti_sudoku))

if __name__ == '__main__':
    main()

