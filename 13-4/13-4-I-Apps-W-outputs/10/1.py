
def get_coating(s, t):
    # Initialize variables
    n = 0
    pieces = []
    
    # Loop through all possible pieces of length 1 to the length of the desired coating
    for i in range(1, len(t) + 1):
        # Loop through all possible starting indices
        for j in range(len(s) - i + 1):
            # Check if the piece is a prefix of the desired coating
            if s[j:j+i] == t[:i]:
                # Add the piece to the list of pieces
                pieces.append((j+1, j+i))
                # Increment the number of pieces needed
                n += 1
    
    # If no pieces were found, return -1
    if n == 0:
        return -1
    
    # Otherwise, return the number of pieces needed and the list of pieces
    return n, pieces

def get_coating_with_glue(s, t):
    # Get the number of pieces needed and the list of pieces
    n, pieces = get_coating(s, t)
    
    # If no pieces were found, return -1
    if n == -1:
        return -1
    
    # Initialize the coating with the first piece
    coating = s[pieces[0][0]-1:pieces[0][1]]
    
    # Loop through the remaining pieces
    for i in range(1, n):
        # Get the current piece
        piece = s[pieces[i][0]-1:pieces[i][1]]
        
        # If the current piece is a prefix of the previous piece, flip it
        if piece == coating[:len(piece)]:
            piece = piece[::-1]
        
        # Add the piece to the coating
        coating += piece
    
    # Return the coating
    return coating

def main():
    # Read the input
    s = input()
    t = input()
    
    # Get the number of pieces needed and the list of pieces
    n, pieces = get_coating(s, t)
    
    # If no pieces were found, print -1
    if n == -1:
        print(-1)
    # Otherwise, print the number of pieces needed and the list of pieces
    else:
        print(n)
        for piece in pieces:
            print(piece[0], piece[1])

if __name__ == '__main__':
    main()

