
def is_possible(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)
    # Iterate through each frequency
    for i, (t_i, n_i) in enumerate(frequencies):
        # Iterate through each interval for the current frequency
        for j in range(n_i):
            # Calculate the start and end positions of the interval
            start_position = positions[i] + t_i * j
            end_position = positions[i] + t_i * (j + 1)
            # Check if the interval overlaps with any of the previous intervals
            for k in range(i):
                if start_position < positions[k] < end_position or positions[k] < start_position < positions[k] + t_i:
                    return "impossible"
            # Update the position of the read/write head for the current frequency
            positions[i] = end_position
    return "possible"

