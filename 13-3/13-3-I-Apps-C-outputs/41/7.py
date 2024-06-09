
def is_possible(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)
    # Initialize a list to store the intervals for each frequency
    intervals = [[0, 0] for _ in range(len(frequencies))]
    # Loop through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        for j in range(n_i):
            # Update the positions of the read/write heads
            positions[i] = (positions[i] + t_i) % 1000000
            # Update the intervals for each frequency
            intervals[i][j] = positions[i]
    # Check if all frequencies can be played as intended
    for i, (t_i, n_i) in enumerate(frequencies):
        for j in range(n_i):
            if intervals[i][j] != intervals[i][j+1]:
                return "impossible"
    return "possible"

