
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the length of the longest balanced string formed by concatenating some of the pieces
    longest_strings = {}
    
    # Iterate over the pieces
    for piece in pieces:
        # If the piece is already a balanced string, add it to the dictionary with its length as the value
        if is_balanced(piece):
            longest_strings[piece] = len(piece)
        # Otherwise, iterate over the substrings of the piece and check if they are balanced
        else:
            for i in range(len(piece)):
                substring = piece[:i]
                if is_balanced(substring):
                    # If the substring is balanced, add it to the dictionary with its length as the value
                    longest_strings[substring] = len(substring)
                    # Check if the substring can be concatenated with other pieces to form a longer balanced string
                    for j in range(i, len(piece)):
                        substring2 = piece[i:j]
                        if substring2 in longest_strings and is_balanced(substring + substring2):
                            longest_strings[substring + substring2] = len(substring + substring2)
    
    # Return the maximum length of the longest balanced string
    return max(longest_strings.values())

# Check if a string is balanced by counting the number of opening and closing parentheses
def is_balanced(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

# Test the function with example input
pieces = [")()", "((()))", "()()"]
print(longest_balanced_string(pieces)) # should print 6

pieces = ["((()))", "()()", "((()))"]
print(longest_balanced_string(pieces)) # should print 6

pieces = ["((()))", "()()", "((()))", "()()"]
print(longest_balanced_string(pieces)) # should print 8

