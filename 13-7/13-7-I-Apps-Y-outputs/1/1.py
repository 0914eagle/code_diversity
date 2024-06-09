
def solve(N, K, M, A):
    # Calculate the current average score
    current_avg = sum(A) / (N-1)
    
    # Check if the goal is already achieved
    if current_avg >= M:
        return 0
    
    # Calculate the minimum points needed to achieve the goal
    min_points = M - current_avg
    
    # Check if the minimum points are within the range of possible scores
    if min_points > K:
        return -1
    
    # Return the minimum points needed to achieve the goal
    return min_points

