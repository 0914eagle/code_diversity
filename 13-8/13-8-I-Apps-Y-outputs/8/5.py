
def solve(picture):
    # Initialize the lists to store the positions of the pieces
    white_pieces = []
    black_pieces = []
    
    # Iterate over the rows of the picture
    for i, row in enumerate(picture):
        # Iterate over the columns of the row
        for j, col in enumerate(row):
            # Check if the current cell is a piece
            if col.isalpha():
                # Get the piece type and color
                piece_type = col.upper()
                piece_color = "White" if i % 2 == 0 else "Black"
                
                # Get the position of the piece
                position = chr(ord('a') + j) + str(i + 1)
                
                # Add the piece to the appropriate list
                if piece_color == "White":
                    white_pieces.append(piece_type + position)
                else:
                    black_pieces.append(piece_type + position)
    
    # Sort the pieces in the lists
    white_pieces.sort()
    black_pieces.sort()
    
    # Return the positions of the pieces in the correct order
    return "White: " + ",".join(white_pieces) + "\nBlack: " + ",".join(black_pieces)

