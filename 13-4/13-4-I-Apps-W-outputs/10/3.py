
def get_min_coatings(s, t):
    # Initialize variables
    n = 0
    coating = ""
    pieces = []
    
    # Loop through the string s and check if it contains the string t
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            # If the string t is found, return the minimum number of coatings needed
            return n
        else:
            # If the string t is not found, add the current piece to the list of pieces
            pieces.append(s[i:i+len(t)])
            n += 1
    
    # If the string t is not found in the entire string s, return -1
    return -1

def get_pieces(s, t):
    # Initialize variables
    pieces = []
    
    # Loop through the string s and check if it contains the string t
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            # If the string t is found, return the list of pieces
            return pieces
        else:
            # If the string t is not found, add the current piece to the list of pieces
            pieces.append(s[i:i+len(t)])
    
    # If the string t is not found in the entire string s, return an empty list
    return []

if __name__ == '__main__':
    s = input()
    t = input()
    print(get_min_coatings(s, t))
    print(*get_pieces(s, t), sep='\n')

