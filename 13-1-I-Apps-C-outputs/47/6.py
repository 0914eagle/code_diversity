
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
            # If the current brightness level is not the favorite brightness level, press the favorite button once
            if curr_brightness != x:
                presses += 1
                curr_brightness = x
            # Press the forward button the appropriate number of times to reach the next brightness level
            presses += abs(curr_brightness - a[i + 1])
            curr_brightness = a[i + 1]
        # If the minimum number of presses is greater than the current number of presses, update the minimum number of presses
        if presses < min_presses:
            min_presses = presses
    # Return the minimum number of presses
    return min_presses

