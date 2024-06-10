
def get_spread(board):
    # Initialize the spread for both players to 0
    mirko_spread, slavko_spread = 0, 0
    
    # Loop through the board and calculate the spread for each player
    for i in range(len(board)):
        for j in range(len(board[0])):
            # If the current field is empty, skip it
            if board[i][j] == '.':
                continue
            
            # If the current field is Mirko's piece, calculate its spread
            if board[i][j] == 'M':
                mirko_spread += calculate_spread(board, i, j, 'M')
            
            # If the current field is Slavko's piece, calculate its spread
            if board[i][j] == 'S':
                slavko_spread += calculate_spread(board, i, j, 'S')
    
    # Return the spread for both players
    return mirko_spread, slavko_spread

def calculate_spread(board, i, j, piece):
    # Initialize the spread to 0
    spread = 0
    
    # Loop through the 8 possible moves for the piece
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        # Calculate the new row and column for the move
        new_i = i + move[0]
        new_j = j + move[1]
        
        # If the new field is outside the board, skip it
        if new_i < 0 or new_i >= len(board) or new_j < 0 or new_j >= len(board[0]):
            continue
        
        # If the new field is empty, skip it
        if board[new_i][new_j] == '.':
            continue
        
        # If the new field is the same piece as the current one, skip it
        if board[new_i][new_j] == piece:
            continue
        
        # Calculate the distance between the current field and the new field
        distance = abs(new_i - i) + abs(new_j - j)
        
        # Add the distance to the spread
        spread += distance
    
    # Return the spread
    return spread

def main():
    # Read the input
    R, C = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(input())
    
    # Calculate the spread for both players
    mirko_spread, slavko_spread = get_spread(board)
    
    # Print the output
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

