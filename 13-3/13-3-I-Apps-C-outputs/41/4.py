
def is_possible(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)

    # Iterate through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        # Iterate through each interval for this frequency
        for j in range(n_i):
            # Calculate the start and end positions of the interval
            start_position = positions[i] + t_i * j
            end_position = positions[i] + t_i * (j + 1)

            # Check if the interval overlaps with any other frequency's interval
            for k in range(len(frequencies)):
                if i != k and start_position < positions[k] < end_position:
                    return "impossible"

            # Update the position of the read/write head for this frequency
            positions[i] = end_position

    return "possible"

