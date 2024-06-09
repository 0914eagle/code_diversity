
def get_min_key_presses(n, lines, r_1, c_1, r_2, c_2):
    # Initialize the minimum number of key presses to infinity
    min_presses = float('inf')

    # Loop through all possible positions of the cursor in the text editor
    for i in range(1, n + 1):
        for j in range(1, lines[i - 1] + 2):
            # Check if the current position is the starting position
            if i == r_1 and j == c_1:
                # Initialize the number of key presses to 0
                presses = 0

                # Loop through all possible positions of the cursor in the text editor
                for k in range(1, n + 1):
                    for l in range(1, lines[k - 1] + 2):
                        # Check if the current position is the ending position
                        if k == r_2 and l == c_2:
                            # Update the minimum number of key presses if necessary
                            min_presses = min(min_presses, presses)

                        # Check if the current position is valid
                        if 1 <= k <= n and 1 <= l <= lines[k - 1] + 1:
                            # Update the number of key presses
                            presses += 1

                            # Check if the current position is the ending position
                            if k == r_2 and l == c_2:
                                # Break the loop
                                break

                            # Check if the current position is the starting position
                            if k == r_1 and l == c_1:
                                # Break the loop
                                break

    # Return the minimum number of key presses
    return min_presses

