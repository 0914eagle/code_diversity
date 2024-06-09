
def get_min_coatings(s, t):
    # Initialize variables
    n = 0
    pieces = []
    coating = ""
    
    # Loop through the characters of the coating t
    for i in range(len(t)):
        # If the current character is not in the coating s, we need to buy a new piece
        if t[i] not in s:
            n += 1
            pieces.append((i, i))
        # If the current character is in the coating s, we can use a piece from the shop
        else:
            # Find the index of the character in the coating s
            j = s.index(t[i])
            # Add the piece to the list of pieces
            pieces.append((j, j+1))
    
    # Return the minimum number of coatings and the list of pieces
    return n, pieces

def get_coating(s, t, pieces):
    # Initialize the coating
    coating = ""
    
    # Loop through the pieces
    for piece in pieces:
        # If the piece is used in the regular order, add it to the coating
        if piece[0] <= piece[1]:
            coating += s[piece[0]:piece[1]+1]
        # If the piece is used in the reversed order, add it to the coating in reverse
        else:
            coating += s[piece[1]-1:piece[0]-1:-1]
    
    # Return the coating
    return coating

if __name__ == '__main__':
    s = input()
    t = input()
    n, pieces = get_min_coatings(s, t)
    coating = get_coating(s, t, pieces)
    print(n)
    for piece in pieces:
        print(piece[0], piece[1])

