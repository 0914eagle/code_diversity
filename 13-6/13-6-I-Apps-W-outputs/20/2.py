
def can_semiknights_meet(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[0])):
            # If the current position is the first semiknight, update its position
            if board[i][j] == "K":
                knight1_row, knight1_col = i, j
            # If the current position is the second semiknight, update its position
            elif board[i][j] == "K":
                knight2_row, knight2_col = i, j
    
    # Check if the semiknights meet in the same square
    if knight1_row == knight2_row and knight1_col == knight2_col:
        return True
    else:
        return False

def main():
    # Read the number of boards from stdin
    num_boards = int(input())
    
    # Loop through each board
    for _ in range(num_boards):
        # Read the board from stdin and convert it to a list of lists
        board = [list(input()) for _ in range(8)]
        
        # Check if the semiknights can meet on the current board
        if can_semiknights_meet(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

