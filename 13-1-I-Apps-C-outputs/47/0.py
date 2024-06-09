
def solve(n, m, a):
    # Initialize the minimum number of presses to infinity
    min_presses = float('inf')
    # Loop through each possible favorite brightness level
    for x in range(1, m + 1):
        # Initialize the current brightness level to the first brightness level
        curr_brightness = a[0]
        # Initialize the number of presses to 0
        presses = 0
        # Loop through each change in brightness
        for i in range(n - 1):
            # If the current brightness level is not the desired brightness level, press the forward button
            if curr_brightness != x:
                presses += 1
                curr_brightness += 1
                if curr_brightness == m + 1:
                    curr_brightness = 1
            # Otherwise, press the favorite button
            else:
                presses += 1
                curr_brightness = x
        # If the current brightness level is not the desired brightness level, press the forward button once
        if curr_brightness != x:
            presses += 1
        # Update the minimum number of presses if necessary
        min_presses = min(min_presses, presses)
    # Return the minimum number of presses
    return min_presses

