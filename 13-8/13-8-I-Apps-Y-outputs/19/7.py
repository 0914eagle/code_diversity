
def solve(x, S):
    # Initialize the maximum value of x
    max_x = 0
    # Loop through each character in S
    for char in S:
        # If the character is 'I', increment x by 1
        if char == 'I':
            x += 1
        # If the character is 'D', decrement x by 1
        elif char == 'D':
            x -= 1
        # Update the maximum value of x
        max_x = max(max_x, x)
    # Return the maximum value of x
    return max_x

