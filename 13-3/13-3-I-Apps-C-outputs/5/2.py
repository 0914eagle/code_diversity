
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the length of the longest balanced string formed by concatenating each piece
    piece_lengths = {}
    for piece in pieces:
        # Check if the piece is balanced
        if is_balanced(piece):
            # If the piece is balanced, add it to the dictionary with its length
            piece_lengths[piece] = len(piece)
    
    # Initialize a variable to store the length of the longest balanced string
    longest_string_length = 0
    
    # Iterate through all possible combinations of pieces
    for i in range(len(pieces)):
        for j in range(i+1, len(pieces)):
            # Concatenate the two pieces and check if the resulting string is balanced
            concatenated_piece = pieces[i] + pieces[j]
            if is_balanced(concatenated_piece):
                # If the resulting string is balanced, update the length of the longest balanced string
                longest_string_length = max(longest_string_length, len(concatenated_piece))
    
    # Return the length of the longest balanced string
    return longest_string_length

def is_balanced(string):
    # Initialize a stack to store the opening parentheses
    stack = []
    for char in string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parenthesis, pop an opening parenthesis from the stack and check if they match
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    # If the stack is empty, the string is balanced
    return len(stack) == 0

def main():
    # Read the number of pieces from stdin
    n = int(input())
    
    # Read the pieces from stdin
    pieces = []
    for i in range(n):
        pieces.append(input())
    
    # Call the longest_balanced_string function and print the result
    print(longest_balanced_string(pieces))

if __name__ == "__main__":
    main()

