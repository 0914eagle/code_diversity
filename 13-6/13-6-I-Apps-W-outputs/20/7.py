
def can_meet(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[0])):
            # If the current position is the first semiknight
            if board[i][j] == "K":
                # Update the position of the first semiknight
                knight1_row, knight1_col = i, j
            # If the current position is the second semiknight
            elif board[i][j] == "k":
                # Update the position of the second semiknight
                knight2_row, knight2_col = i, j
    
    # If the first semiknight is in the same position as the second semiknight
    if knight1_row == knight2_row and knight1_col == knight2_col:
        return True
    else:
        return False

def main():
    # Read the number of boards
    num_boards = int(input())
    
    # Loop through each board
    for i in range(num_boards):
        # Read the board
        board = [input() for _ in range(8)]
        
        # Check if the semiknights can meet
        if can_meet(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

