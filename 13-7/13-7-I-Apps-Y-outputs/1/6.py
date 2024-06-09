
def solve(N, K, M, A):
    # Calculate the sum of the scores already achieved
    sum_of_scores = sum(A)
    # Calculate the minimum number of points needed to achieve the goal
    min_points = M - (sum_of_scores / (N-1))
    # Check if the minimum number of points is possible
    if min_points < 0:
        return -1
    else:
        return min_points

