
def can_semiknights_meet(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight_1_row, knight_1_col = 0, 0
    knight_2_row, knight_2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[0])):
            # If the current position is the first semiknight, update its position
            if board[i][j] == "K":
                knight_1_row, knight_1_col = i, j
            # If the current position is the second semiknight, update its position
            elif board[i][j] == "k":
                knight_2_row, knight_2_col = i, j
    
    # Check if the semiknights can meet by checking if their positions are the same
    if knight_1_row == knight_2_row and knight_1_col == knight_2_col:
        return True
    else:
        return False

def main():
    num_boards = int(input())
    for i in range(num_boards):
        board = []
        for j in range(8):
            board.append(input())
        if can_semiknights_meet(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

