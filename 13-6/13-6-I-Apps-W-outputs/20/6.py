
def can_semiknights_meet(board):
    # Initialize variables to keep track of the positions of the semiknights
    knight1_row, knight1_col = 0, 0
    knight2_row, knight2_col = 0, 0
    
    # Initialize a set to keep track of the bad squares
    bad_squares = set()
    
    # Iterate through the board and find the positions of the semiknights and the bad squares
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "K":
                if knight1_row == 0 and knight1_col == 0:
                    knight1_row, knight1_col = row, col
                else:
                    knight2_row, knight2_col = row, col
            elif board[row][col] == "#":
                bad_squares.add((row, col))
    
    # Function to check if a square is valid for the semiknights to meet
    def is_valid_square(row, col):
        return (row, col) not in bad_squares and row in range(8) and col in range(8)
    
    # Function to move the semiknights and check if they meet
    def move_semiknights():
        nonlocal knight1_row, knight1_col, knight2_row, knight2_col
        # Move the first semiknight
        if is_valid_square(knight1_row + 2, knight1_col + 2):
            knight1_row += 2
            knight1_col += 2
        elif is_valid_square(knight1_row + 2, knight1_col - 2):
            knight1_row += 2
            knight1_col -= 2
        elif is_valid_square(knight1_row - 2, knight1_col + 2):
            knight1_row -= 2
            knight1_col += 2
        elif is_valid_square(knight1_row - 2, knight1_col - 2):
            knight1_row -= 2
            knight1_col -= 2
        # Move the second semiknight
        if is_valid_square(knight2_row + 2, knight2_col + 2):
            knight2_row += 2
            knight2_col += 2
        elif is_valid_square(knight2_row + 2, knight2_col - 2):
            knight2_row += 2
            knight2_col -= 2
        elif is_valid_square(knight2_row - 2, knight2_col + 2):
            knight2_row -= 2
            knight2_col += 2
        elif is_valid_square(knight2_row - 2, knight2_col - 2):
            knight2_row -= 2
            knight2_col -= 2
        # Check if the semiknights meet
        if knight1_row == knight2_row and knight1_col == knight2_col:
            return True
        return False
    
    # Iterate through the board and move the semiknights until they meet
    while not move_semiknights():
        pass
    
    # If the semiknights meet, return "YES", otherwise return "NO"
    if knight1_row == knight2_row and knight1_col == knight2_col:
        return "YES"
    else:
        return "NO"

def main():
    num_boards = int(input())
    for _ in range(num_boards):
        board = [input() for _ in range(8)]
        print(can_semiknights_meet(board))

if __name__ == '__main__':
    main()

