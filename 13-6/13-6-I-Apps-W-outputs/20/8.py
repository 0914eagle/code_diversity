
def can_semiknights_meet(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[i])):
            # If the current square is the position of the first semiknight
            if board[i][j] == "K":
                # Update the position of the first semiknight
                knight1_row, knight1_col = i, j
            # If the current square is the position of the second semiknight
            elif board[i][j] == "k":
                # Update the position of the second semiknight
                knight2_row, knight2_col = i, j
    
    # If the positions of the semiknights are the same, they can meet
    if knight1_row == knight2_row and knight1_col == knight2_col:
        return True
    # Otherwise, they cannot meet
    else:
        return False

def solve(board):
    # Check if the semiknights can meet on the current board
    if can_semiknights_meet(board):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    num_boards = int(input())
    for _ in range(num_boards):
        board = [input() for _ in range(8)]
        print(solve(board))

