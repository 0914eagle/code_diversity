
def solve(walk):
    # Initialize the value of the walk as 1
    value = 1

    # Iterate through the walk string
    for char in walk:
        # If the character is 'L', multiply the value by 2
        if char == 'L':
            value *= 2
        # If the character is 'R', add 1 to the value
        elif char == 'R':
            value += 1
        # If the character is 'P', do nothing
        elif char == 'P':
            pass
        # If the character is '*', multiply the value by 2 and add 1
        elif char == '*':
            value *= 2
            value += 1

    # Return the final value of the walk
    return value

