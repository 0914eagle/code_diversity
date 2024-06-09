
def is_possible(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)
    # Initialize a list to store the intervals for each frequency
    intervals = [[0, 0] for _ in range(len(frequencies))]
    # Loop through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        for j in range(n_i):
            t_ij = intervals[i][j * 2] = int(input())
            t_i_j_plus_1 = intervals[i][j * 2 + 1] = int(input())
            # Check if the interval overlaps with any previous interval
            for k in range(i):
                if intervals[k][-1] > t_ij or intervals[k][0] < t_i_j_plus_1:
                    return "impossible"
            # Update the position of the read/write head for this frequency
            positions[i] = t_i_j_plus_1
    return "possible"

