
def is_meeting_possible(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight_1_row, knight_1_col = 0, 0
    knight_2_row, knight_2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the current row
        for j in range(len(board[i])):
            # If the current square is the first semiknight, update its position
            if board[i][j] == "K":
                knight_1_row, knight_1_col = i, j
            # If the current square is the second semiknight, update its position
            elif board[i][j] == "K":
                knight_2_row, knight_2_col = i, j
    
    # Calculate the distance between the two semiknights
    dist_x = abs(knight_1_col - knight_2_col)
    dist_y = abs(knight_1_row - knight_2_row)
    
    # If the distance between the two semiknights is even, they can meet
    if dist_x % 2 == 0 and dist_y % 2 == 0:
        return True
    else:
        return False

def main():
    # Read the number of boards
    num_boards = int(input())
    
    # Loop through each board
    for i in range(num_boards):
        # Read the board
        board = []
        for j in range(8):
            board.append(list(input()))
        
        # Check if the semiknights can meet
        if is_meeting_possible(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

