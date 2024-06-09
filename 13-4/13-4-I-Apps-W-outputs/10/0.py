
def get_min_coatings(s, t):
    # Initialize variables
    n = 0
    pieces = []
    coating = ""
    
    # Loop through the characters of the string t
    for i in range(len(t)):
        # If the current character is not in the coating, add it to the coating and increment the number of coatings needed
        if t[i] not in coating:
            n += 1
            coating += t[i]
        # If the current character is already in the coating, find the index of the character in the coating and add the piece to the pieces list
        else:
            index = coating.index(t[i])
            pieces.append((index, i))
    
    # Sort the pieces list by the index of the character in the coating
    pieces.sort(key=lambda x: x[0])
    
    # If the number of coatings needed is greater than the length of the string s, return -1
    if n > len(s):
        return -1
    
    # Initialize the output list
    output = []
    
    # Loop through the pieces list
    for piece in pieces:
        # If the index of the character in the coating is less than or equal to the index of the character in the string s, add the piece to the output list
        if piece[0] <= piece[1]:
            output.append(piece)
        # If the index of the character in the coating is greater than the index of the character in the string s, add the piece to the output list and flip it
        else:
            output.append((piece[1], piece[0]))
    
    # Return the number of coatings needed and the output list
    return n, output

def get_coating(s, t):
    # Get the minimum number of coatings needed and the pieces list
    n, pieces = get_min_coatings(s, t)
    
    # If the number of coatings needed is -1, return -1
    if n == -1:
        return -1
    
    # Initialize the coating
    coating = ""
    
    # Loop through the pieces list
    for piece in pieces:
        # If the piece is not flipped, add the corresponding substring to the coating
        if piece[0] <= piece[1]:
            coating += s[piece[0]:piece[1] + 1]
        # If the piece is flipped, add the corresponding substring to the coating in reverse order
        else:
            coating += s[piece[1]:piece[0] + 1][::-1]
    
    # Return the coating
    return coating

if __name__ == '__main__':
    s = input()
    t = input()
    n, pieces = get_min_coatings(s, t)
    if n == -1:
        print(-1)
    else:
        print(n)
        for piece in pieces:
            print(piece[0], piece[1])

