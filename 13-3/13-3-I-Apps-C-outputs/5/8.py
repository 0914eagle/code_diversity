
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the lengths of the balanced strings for each piece
    piece_lengths = {}
    # Iterate over the pieces and calculate the length of the balanced string for each piece
    for piece in pieces:
        piece_lengths[piece] = len(balanced_string(piece))
    # Initialize a variable to store the longest balanced string length
    longest_length = 0
    # Iterate over the pieces and calculate the longest balanced string length by concatenating some of the pieces
    for i in range(len(pieces)):
        for j in range(i, len(pieces)):
            piece1 = pieces[i]
            piece2 = pieces[j]
            concatenated_pieces = piece1 + piece2
            longest_length = max(longest_length, piece_lengths[concatenated_pieces])
    return longest_length

def balanced_string(string):
    # Initialize a stack to store the opening parentheses
    stack = []
    # Iterate over the characters in the string
    for char in string:
        # If the character is an opening parentheses, push it to the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parentheses, pop an opening parentheses from the stack and check if they match
        elif char == ')':
            if not stack or stack[-1] != '(':
                return ""
            stack.pop()
    # If the stack is empty, the string is balanced
    if not stack:
        return string
    # If the stack is not empty, the string is not balanced
    return ""

