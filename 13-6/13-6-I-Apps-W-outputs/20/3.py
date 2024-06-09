
def can_semiknights_meet(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the current row
        for j in range(len(board[i])):
            # Check if the current square is a semiknight
            if board[i][j] == "K":
                # If it's the first semiknight, set its position
                if knight1_row == 0 and knight1_col == 0:
                    knight1_row, knight1_col = i, j
                # If it's the second semiknight, set its position
                elif knight2_row == 0 and knight2_col == 0:
                    knight2_row, knight2_col = i, j
    
    # Calculate the distance between the two semiknights
    dist = abs(knight1_row - knight2_row) + abs(knight1_col - knight2_col)
    
    # If the distance is even, the semiknights can meet
    if dist % 2 == 0:
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
        if can_semiknights_meet(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

