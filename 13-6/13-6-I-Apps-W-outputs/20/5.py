
def can_meet(board):
    # Initialize variables to keep track of the positions of the knights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Loop through each row of the board
    for row in range(len(board)):
        # Loop through each column of the current row
        for col in range(len(board[row])):
            # Check if the current square is occupied by a knight
            if board[row][col] == "K":
                # If it is the first knight, save its position
                if knight1_row == 0 and knight1_col == 0:
                    knight1_row, knight1_col = row, col
                # If it is the second knight, save its position
                else:
                    knight2_row, knight2_col = row, col
    
    # Initialize a set to keep track of the visited squares
    visited = set()
    
    # Loop through each possible move for the first knight
    for i in range(2):
        for j in range(2):
            # Calculate the new position of the first knight
            new_row = knight1_row + i
            new_col = knight1_col + j
            
            # Check if the new position is valid and has not been visited before
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and (new_row, new_col) not in visited:
                # Add the new position to the visited set
                visited.add((new_row, new_col))
                
                # Check if the new position is the same as the second knight's position
                if (new_row, new_col) == (knight2_row, knight2_col):
                    return True
    
    # If the first knight cannot reach the second knight, return False
    return False

def main():
    # Read the number of boards
    num_boards = int(input())
    
    # Loop through each board
    for _ in range(num_boards):
        # Read the board
        board = [input() for _ in range(8)]
        
        # Check if the knights can meet
        if can_meet(board):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

