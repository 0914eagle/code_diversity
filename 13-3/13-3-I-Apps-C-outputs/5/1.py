
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the lengths of the balanced strings for each piece
    piece_lengths = {}
    # Iterate over the pieces and calculate the length of the balanced string for each piece
    for piece in pieces:
        piece_lengths[piece] = len(piece)
    # Initialize a list to store the longest balanced string formed by concatenating some of the pieces
    longest_string = []
    # Iterate over the pieces and try to form the longest balanced string by concatenating some of them
    for piece in pieces:
        # If the piece is already part of the longest string, skip it
        if piece in longest_string:
            continue
        # If the piece is not balanced, skip it
        if not is_balanced(piece):
            continue
        # If the piece is balanced, try to form the longest balanced string by concatenating it with the current longest string
        longest_string.append(piece)
        # If the concatenated string is not balanced, remove the piece from the longest string
        if not is_balanced("".join(longest_string)):
            longest_string.pop()
    # Return the length of the longest balanced string
    return len("".join(longest_string))

def is_balanced(string):
    # Initialize a stack to store the opening parentheses
    stack = []
    # Iterate over the characters in the string
    for char in string:
        # If the character is an opening parenthesis, push it to the stack
        if char == "(":
            stack.append(char)
        # If the character is a closing parenthesis, pop an opening parenthesis from the stack
        elif char == ")":
            stack.pop()
        # If the stack is empty and there are still characters left in the string, the string is not balanced
        if not stack and string:
            return False
    # If the stack is empty and there are no more characters left in the string, the string is balanced
    return not stack

pieces = ["())", "((()))", ")()"]
print(longest_balanced_string(pieces))

