
def is_possible(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)
    # Initialize a list to store the intervals for each frequency
    intervals = [[0, 0] for _ in range(len(frequencies))]
    # Loop through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        for j in range(n_i):
            t_ij, t_i_j_plus_1 = map(int, input().split())
            intervals[i].append((t_ij, t_i_j_plus_1))
    # Sort the intervals for each frequency in ascending order
    for i in range(len(frequencies)):
        intervals[i].sort()
    # Loop through each interval and check if the read/write head can reach it
    for i in range(len(frequencies)):
        for j in range(len(intervals[i]) - 1):
            t_ij, t_i_j_plus_1 = intervals[i][j]
            t_i_j_plus_2, t_i_j_plus_3 = intervals[i][j + 1]
            if t_i_j_plus_1 - t_ij != t_i_j_plus_3 - t_i_j_plus_2:
                return "impossible"
    return "possible"

