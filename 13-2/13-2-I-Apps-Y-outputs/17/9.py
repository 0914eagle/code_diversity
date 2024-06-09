
def solve(n, a):
    # Initialize a set to store the indices of the buttons that are lighten up
    lighten_up = set()
    # Add the index of Button 1 to the set
    lighten_up.add(1)
    # Initialize a variable to store the minimum number of times we need to press buttons
    min_presses = 0
    # Loop through the indices of the buttons
    for i in range(1, n + 1):
        # If the current button is lighten up and its index is not equal to Button 2, press the button
        if i in lighten_up and i != 2:
            # Add the index of the button that will be lighten up after pressing the current button to the set
            lighten_up.add(a[i - 1])
            # Increment the minimum number of times we need to press buttons
            min_presses += 1
    # If Button 2 is not lighten up, return -1
    if 2 not in lighten_up:
        return -1
    # Otherwise, return the minimum number of times we need to press buttons
    return min_presses

