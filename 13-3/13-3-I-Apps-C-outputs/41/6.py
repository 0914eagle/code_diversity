
def is_possible(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)
    # Initialize a list to store the intervals for each frequency
    intervals = [[] for _ in range(len(frequencies))]
    # Loop through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        for j in range(n_i):
            t_ij = t_i * j
            t_i_j_plus_1 = t_i * (j + 1)
            intervals[i].append((t_ij, t_i_j_plus_1))
    # Loop through each interval and check if the read/write head is at the correct position
    for t in range(max(map(max, intervals))):
        for i, (t_i, n_i) in enumerate(frequencies):
            for j in range(n_i):
                t_ij = t_i * j
                t_i_j_plus_1 = t_i * (j + 1)
                if t_ij <= t < t_i_j_plus_1:
                    positions[i] = t
                    break
        else:
            continue
        for i in range(len(frequencies)):
            if positions[i] != intervals[i][j][0]:
                return "impossible"
    return "possible"

