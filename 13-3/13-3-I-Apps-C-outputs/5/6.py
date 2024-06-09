
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the length of the longest balanced string formed by concatenating each piece
    piece_lengths = {}
    # Initialize the longest balanced string as the empty string
    longest_string = ""

    for piece in pieces:
        # Check if the piece is already in the dictionary
        if piece not in piece_lengths:
            # If not, calculate the length of the longest balanced string formed by concatenating the piece with each of the other pieces
            for other_piece in pieces:
                if piece != other_piece:
                    # Concatenate the piece with the other piece and check if the result is a balanced string
                    concatenated_piece = piece + other_piece
                    if is_balanced(concatenated_piece):
                        # If it is, store the length of the concatenated string in the dictionary
                        piece_lengths[piece] = len(concatenated_piece)
        # If the piece is already in the dictionary, skip it

    # Find the piece with the longest length in the dictionary
    for piece, length in piece_lengths.items():
        if length > len(longest_string):
            longest_string = piece * length

    return len(longest_string)

def is_balanced(string):
    # Initialize a stack to keep track of the parentheses
    stack = []
    # Iterate through the string
    for char in string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the character is a closing parenthesis, pop an opening parenthesis from the stack
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    # If the stack is empty, the string is balanced
    return len(stack) == 0

def main():
    num_pieces = int(input())
    pieces = []
    for i in range(num_pieces):
        pieces.append(input())
    print(longest_balanced_string(pieces))

if __name__ == "__main__":
    main()

