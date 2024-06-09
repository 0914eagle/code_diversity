
def get_min_key_presses(n, a, r_1, c_1, r_2, c_2):
    # Initialize the minimum number of key presses to infinity
    min_presses = float('inf')

    # Loop through all possible positions of the cursor in the text editor
    for i in range(n):
        for j in range(a[i] + 1):
            # If the current position is (r_1, c_1), update the minimum number of key presses
            if i == r_1 and j == c_1:
                min_presses = min(min_presses, get_key_presses(n, a, i, j, r_2, c_2))

    # Return the minimum number of key presses
    return min_presses

# Function to get the number of key presses to move the cursor from position (i, j) to position (r_2, c_2)
def get_key_presses(n, a, i, j, r_2, c_2):
    # Initialize the number of key presses to 0
    presses = 0

    # Loop until the cursor reaches the final position (r_2, c_2)
    while i != r_2 or j != c_2:
        # If the cursor is in the last line and the final position is not in this line, move the cursor up
        if i == n - 1 and j > c_2:
            presses += 1
            i -= 1
        # If the cursor is in the first line and the final position is not in this line, move the cursor down
        elif i == 1 and j < c_2:
            presses += 1
            i += 1
        # If the cursor is in the middle of the text editor and the final position is in the previous line, move the cursor up
        elif i > 1 and j > c_2:
            presses += 1
            i -= 1
        # If the cursor is in the middle of the text editor and the final position is in the next line, move the cursor down
        elif i < n and j < c_2:
            presses += 1
            i += 1
        # If the cursor is in the last line and the final position is in this line, move the cursor to the left
        elif i == n - 1 and j == c_2:
            presses += 1
            j -= 1
        # If the cursor is in the first line and the final position is in this line, move the cursor to the right
        elif i == 1 and j == c_2:
            presses += 1
            j += 1
        # If the cursor is in the middle of the text editor and the final position is in the previous line, move the cursor to the left
        elif i > 1 and j == c_2:
            presses += 1
            j -= 1
        # If the cursor is in the middle of the text editor and the final position is in the next line, move the cursor to the right
        elif i < n and j == c_2:
            presses += 1
            j += 1

    # Return the number of key presses
    return presses

