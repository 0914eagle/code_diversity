
def get_anti_sudoku(sudoku):
    # Initialize a dictionary to store the counts of each number in each row, column, and block
    row_counts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    col_counts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    block_counts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    
    # Loop through each cell in the sudoku and update the counts
    for i in range(9):
        for j in range(9):
            num = int(sudoku[i][j])
            row = i // 3
            col = j // 3
            block = (row // 3) * 3 + col // 3
            if num not in row_counts[i]:
                row_counts[i][num] = 1
            else:
                row_counts[i][num] += 1
            if num not in col_counts[j]:
                col_counts[j][num] = 1
            else:
                col_counts[j][num] += 1
            if num not in block_counts[block]:
                block_counts[block][num] = 1
            else:
                block_counts[block][num] += 1
    
    # Loop through each cell in the sudoku and check if it can be changed to make it anti-sudoku
    for i in range(9):
        for j in range(9):
            num = int(sudoku[i][j])
            row = i // 3
            col = j // 3
            block = (row // 3) * 3 + col // 3
            if row_counts[i][num] == 1 and col_counts[j][num] == 1 and block_counts[block][num] == 1:
                return (i, j)
    return None

def main():
    t = int(input())
    for _ in range(t):
        sudoku = [input() for _ in range(9)]
        print(get_anti_sudoku(sudoku))

if __name__ == '__main__':
    main()

