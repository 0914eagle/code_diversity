
def solve_magic_checkerboard(n, m, board):
    # Initialize a dictionary to store the parity of each row and column
    row_parity = {}
    col_parity = {}
    
    # Iterate through the board and check if the values in each row and column are in strictly increasing order
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                # Check if the value is in the correct row
                if i in row_parity and row_parity[i] != board[i][j] % 2:
                    return -1
                # Check if the value is in the correct column
                if j in col_parity and col_parity[j] != board[i][j] % 2:
                    return -1
                # Add the parity of the value to the row and column dictionaries
                row_parity[i] = board[i][j] % 2
                col_parity[j] = board[i][j] % 2
    
    # Initialize a list to store the filled board
    filled_board = []
    
    # Iterate through the board and fill in the 0 cells
    for i in range(n):
        filled_row = []
        for j in range(m):
            if board[i][j] == 0:
                # Find the next available value in the row and column
                next_val = 1
                while next_val in row_parity[i] or next_val in col_parity[j]:
                    next_val += 1
                # Add the value to the row and column dictionaries
                row_parity[i].add(next_val)
                col_parity[j].add(next_val)
                # Add the value to the filled board
                filled_row.append(next_val)
            else:
                filled_row.append(board[i][j])
        filled_board.append(filled_row)
    
    # Calculate the sum of the filled board
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += filled_board[i][j]
    
    return sum

