
def get_anti_sudoku(sudoku):
    # Initialize a list to store the changed elements
    changed_elements = []
    
    # Iterate through the rows
    for i in range(9):
        # Get the row as a list of integers
        row = [int(x) for x in sudoku[i]]
        
        # Check if the row contains duplicates
        if len(set(row)) < 9:
            # Get the indices of the duplicates
            duplicates = [i for i, x in enumerate(row) if row.count(x) > 1]
            
            # Change the value of the first duplicate to any other value in the range [1, 9]
            changed_elements.append((i, duplicates[0], random.randint(1, 9)))
    
    # Iterate through the columns
    for j in range(9):
        # Get the column as a list of integers
        col = [int(sudoku[i][j]) for i in range(9)]
        
        # Check if the column contains duplicates
        if len(set(col)) < 9:
            # Get the indices of the duplicates
            duplicates = [j for j, x in enumerate(col) if col.count(x) > 1]
            
            # Change the value of the first duplicate to any other value in the range [1, 9]
            changed_elements.append((duplicates[0], j, random.randint(1, 9)))
    
    # Iterate through the 3x3 blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # Get the block as a list of integers
            block = [int(sudoku[x][y]) for x in range(i, i + 3) for y in range(j, j + 3)]
            
            # Check if the block contains duplicates
            if len(set(block)) < 9:
                # Get the indices of the duplicates
                duplicates = [((x, y) for x in range(i, i + 3) for y in range(j, j + 3) if block.count(sudoku[x][y]) > 1)]
                
                # Change the value of the first duplicate to any other value in the range [1, 9]
                changed_elements.append((duplicates[0][0], duplicates[0][1], random.randint(1, 9)))
    
    # Return the changed elements
    return changed_elements

def main():
    # Read the input
    t = int(input())
    sudokus = [input() for _ in range(t)]
    
    # Iterate through the sudokus
    for sudoku in sudokus:
        # Get the anti-sudoku
        changed_elements = get_anti_sudoku(sudoku)
        
        # Print the anti-sudoku
        for i, j, value in changed_elements:
            sudoku = list(sudoku)
            sudoku[i] = sudoku[i][:j] + str(value) + sudoku[i][j + 1:]
        print(''.join(sudoku))

if __name__ == '__main__':
    main()

