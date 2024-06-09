
def solve(n, b, a, s):
    # Initialize the maximum number of segments as 0
    max_segments = 0
    # Initialize the current battery and accumulator charges as the given values
    battery, accumulator = b, a
    # Iterate through the segments
    for i in range(n):
        # If the segment is exposed to sunlight and the battery is not empty
        if s[i] == 1 and battery > 0:
            # Decrease the battery charge by 1
            battery -= 1
            # Increase the accumulator charge by 1
            accumulator += 1
        # If the accumulator is not empty
        if accumulator > 0:
            # Decrease the accumulator charge by 1
            accumulator -= 1
        # If the battery is not empty
        if battery > 0:
            # Decrease the battery charge by 1
            battery -= 1
        # Update the maximum number of segments if the current number of segments is greater than the previous maximum
        max_segments = max(max_segments, i+1)
    # Return the maximum number of segments
    return max_segments

