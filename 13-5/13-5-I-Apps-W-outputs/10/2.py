
def get_min_key_presses(n, lines, r_1, c_1, r_2, c_2):
    # Initialize the minimum number of key presses to infinity
    min_presses = float('inf')

    # Loop through all possible positions of the cursor in the text editor
    for i in range(n):
        for j in range(1, lines[i] + 1):
            # Calculate the number of key presses needed to move the cursor from (r_1, c_1) to (i, j)
            presses = abs(r_1 - i) + abs(c_1 - j)

            # If the number of key presses is less than the minimum, update the minimum
            if presses < min_presses:
                min_presses = presses

    # Return the minimum number of key presses
    return min_presses

