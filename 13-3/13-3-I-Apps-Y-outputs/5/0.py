
def solve(N, K, x):
    # Calculate the minimum distance covered by each robot
    dist_A = sum([abs(x_i - K) for x_i in x])
    dist_B = sum([abs(x_i) for x_i in x])

    # Return the minimum distance covered
    return min(dist_A, dist_B)

