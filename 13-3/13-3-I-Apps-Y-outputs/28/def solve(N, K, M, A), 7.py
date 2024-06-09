
def solve(N, K, M, A):
    # Calculate the current average score
    current_average = sum(A) / (N-1)
    
    # Check if the goal is already achieved
    if current_average >= M:
        return 0
    
    # Calculate the minimum number of points needed to achieve the goal
    min_points = M - current_average
    
    # Check if the minimum number of points is possible to achieve
    if min_points > K:
        return -1
    
    # Return the minimum number of points needed to achieve the goal
    return min_points

