
def solve(N, K, M, A):
    # Calculate the current average score
    current_average = sum(A) / (N-1)
    
    # Check if the goal is achievable
    if current_average >= M:
        return -1
    
    # Calculate the minimum number of points needed on the final subject
    min_points = (M - current_average) * (N-1) / N
    
    return min_points

