
def solve(N, K, x):
    # Calculate the minimum distance covered by each robot
    min_dist_A = sum([abs(x_i - K) for x_i in x])
    min_dist_B = sum([abs(x_i) for x_i in x])

    # Return the minimum of the two distances
    return min(min_dist_A, min_dist_B)

