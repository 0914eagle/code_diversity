
def solve(walk):
    # Initialize the value of the walk to 0
    value = 0
    
    # Iterate through each character in the walk
    for char in walk:
        # If the character is 'L', add 2 to the value
        if char == 'L':
            value += 2
        # If the character is 'R', add 1 to the value
        elif char == 'R':
            value += 1
        # If the character is 'P', do nothing
        elif char == 'P':
            pass
        # If the character is '*', add the value of the walk to the current value
        elif char == '*':
            value += value
    
    # Return the final value of the walk
    return value

