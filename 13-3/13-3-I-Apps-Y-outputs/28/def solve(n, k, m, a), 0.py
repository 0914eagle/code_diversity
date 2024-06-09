
def solve(n, k, m, a):
    # Calculate the sum of the scores already achieved
    sum_a = sum(a)
    # Calculate the minimum number of points needed to achieve the goal
    min_points = m * (n - len(a)) - sum_a
    # Check if the minimum number of points is possible
    if min_points < 0:
        return -1
    # Return the minimum number of points needed
    return min_points

