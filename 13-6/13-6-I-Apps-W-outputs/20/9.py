
def can_meet(board):
    # Initialize variables to keep track of the positions of the knights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the current row
        for j in range(len(board[i])):
            # Check if the current square is the position of the first knight
            if board[i][j] == "K":
                # Update the position of the first knight
                knight1_row, knight1_col = i, j
            # Check if the current square is the position of the second knight
            elif board[i][j] == "k":
                # Update the position of the second knight
                knight2_row, knight2_col = i, j
    
    # Check if the knights have met
    if knight1_row == knight2_row and knight1_col == knight2_col:
        return True
    else:
        return False

def main():
    # Read the number of boards
    num_boards = int(input())
    
    # Loop through each board
    for i in range(num_boards):
        # Read the current board
        board = [input() for _ in range(8)]
        
        # Check if the knights can meet on the current board
        if can_meet(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

