
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the lengths of the balanced strings for each piece
    piece_lengths = {}
    # Iterate over the pieces and calculate the length of the balanced string for each piece
    for piece in pieces:
        piece_lengths[piece] = len(balanced_string(piece))
    # Initialize a variable to store the longest balanced string length
    longest_length = 0
    # Iterate over the pieces and try to form the longest balanced string by concatenating them
    for i in range(len(pieces)):
        for j in range(i, len(pieces)):
            piece1 = pieces[i]
            piece2 = pieces[j]
            concatenated_pieces = piece1 + piece2
            if balanced_string(concatenated_pieces) and len(concatenated_pieces) > longest_length:
                longest_length = len(concatenated_pieces)
    return longest_length

def balanced_string(s):
    # Initialize a stack to store the opening parentheses
    stack = []
    # Iterate over the characters in the string
    for char in s:
        # If the character is an opening parentheses, push it to the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parentheses, pop an opening parentheses from the stack
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    # If the stack is empty, the string is balanced
    return not stack

pieces = ["())", "((()))", "()()"]
print(longest_balanced_string(pieces))

