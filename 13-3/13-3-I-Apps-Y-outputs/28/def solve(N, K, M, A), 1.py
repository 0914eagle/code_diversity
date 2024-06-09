
def solve(N, K, M, A):
    # Calculate the sum of the scores already obtained
    total = sum(A)
    # Calculate the minimum number of points needed to achieve the goal
    min_points = M * (N - len(A)) + (K - total)
    # If the minimum number of points is greater than or equal to 0, return it
    if min_points >= 0:
        return min_points
    # If the minimum number of points is less than 0, the goal is unachievable
    else:
        return -1

