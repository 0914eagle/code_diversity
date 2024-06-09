
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the lengths of the balanced strings for each piece
    piece_lengths = {}
    # Iterate over the pieces and calculate the length of the balanced string for each piece
    for piece in pieces:
        piece_lengths[piece] = len(balanced_string(piece))
    # Initialize the longest balanced string length to 0
    longest_length = 0
    # Iterate over the pieces and try to form the longest balanced string by concatenating some of them in some order
    for i in range(len(pieces)):
        for j in range(i, len(pieces)):
            piece1 = pieces[i]
            piece2 = pieces[j]
            # Check if the concatenation of the two pieces is a balanced string
            if is_balanced(piece1 + piece2):
                # Calculate the length of the concatenated string
                length = piece_lengths[piece1] + piece_lengths[piece2]
                # Update the longest balanced string length if necessary
                longest_length = max(longest_length, length)
    return longest_length

def balanced_string(string):
    # Initialize a stack to store the parentheses
    stack = []
    # Iterate over the characters in the string
    for char in string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parenthesis, pop an opening parenthesis from the stack
        elif char == ')':
            stack.pop()
    # If the stack is empty, the string is balanced
    return '' if not stack else None

def is_balanced(string):
    # Check if the string is balanced
    return balanced_string(string) is None

def main():
    # Read the number of pieces from stdin
    n = int(input())
    # Read the pieces from stdin
    pieces = [input() for _ in range(n)]
    # Find the longest balanced string
    longest_length = longest_balanced_string(pieces)
    # Print the longest balanced string length
    print(longest_length)

if __name__ == "__main__":
    main()

