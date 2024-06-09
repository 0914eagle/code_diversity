
def solve(walk):
    # Initialize the value of the walk as 0
    value = 0
    
    # Iterate through each character in the walk
    for char in walk:
        # If the character is 'L', add 1 to the value
        if char == 'L':
            value += 1
        # If the character is 'R', add 2 to the value
        elif char == 'R':
            value += 2
        # If the character is 'P', add 0 to the value
        elif char == 'P':
            value += 0
        # If the character is '*', add 3 to the value
        elif char == '*':
            value += 3
    
    # Return the final value of the walk
    return value

