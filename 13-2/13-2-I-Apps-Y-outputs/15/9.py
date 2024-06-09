
def solve(n, b, a, s):
    # Initialize the maximum number of segments as 0
    max_segments = 0
    # Initialize the current battery and accumulator charges as the given values
    battery, accumulator = b, a
    # Iterate through the segments
    for i in range(n):
        # If the current segment is exposed to sunlight and the battery is not empty
        if s[i] == 1 and battery > 0:
            # Use the battery to pass the segment and decrease the battery charge by 1
            battery -= 1
            # Increase the accumulator charge by 1
            accumulator += 1
        # If the accumulator is not empty
        elif accumulator > 0:
            # Use the accumulator to pass the segment and decrease the accumulator charge by 1
            accumulator -= 1
        # If the battery and accumulator are empty, break the loop
        else:
            break
        # Increase the maximum number of segments by 1
        max_segments += 1
    # Return the maximum number of segments
    return max_segments

