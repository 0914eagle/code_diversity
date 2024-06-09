
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the length of the longest balanced string formed by concatenating each piece
    piece_lengths = {}
    for piece in pieces:
        # Check if the piece is already in the dictionary
        if piece in piece_lengths:
            # If it is, skip this piece
            continue
        # If it's not, find the length of the longest balanced string that can be formed by concatenating this piece with some other piece
        longest_length = 0
        for other_piece in pieces:
            if piece == other_piece:
                # Skip this piece if it's the same as the current piece
                continue
            # Concatenate the two pieces and check if the result is a balanced string
            concatenated_piece = piece + other_piece
            if is_balanced(concatenated_piece):
                # If it is, update the length of the longest balanced string formed by concatenating this piece
                longest_length = max(longest_length, len(concatenated_piece))
        # Add the length of the longest balanced string formed by concatenating this piece to the dictionary
        piece_lengths[piece] = longest_length
    
    # Find the maximum length of all the pieces
    max_length = max(piece_lengths.values())
    
    # Return the maximum length
    return max_length

def is_balanced(string):
    # Initialize a stack to keep track of the parentheses
    stack = []
    for char in string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parenthesis, pop an opening parenthesis from the stack
        elif char == ')':
            if len(stack) == 0:
                # If the stack is empty, the string is not balanced
                return False
            stack.pop()
    
    # If the stack is empty, the string is balanced
    return len(stack) == 0

def main():
    # Read the number of pieces from stdin
    n = int(input())
    
    # Read the pieces from stdin
    pieces = []
    for i in range(n):
        pieces.append(input())
    
    # Find the longest balanced string
    longest_string = longest_balanced_string(pieces)
    
    # Print the length of the longest balanced string
    print(longest_string)

if __name__ == "__main__":
    main()

