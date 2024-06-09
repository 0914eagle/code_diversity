
def solve(N, K, x):
    # Calculate the total distance covered by each robot
    total_distance_A = 0
    total_distance_B = 0
    for i in range(N):
        total_distance_A += abs(x[i] - 0) + abs(x[i] - 0)
        total_distance_B += abs(x[i] - K) + abs(x[i] - K)
    
    # Return the minimum total distance
    return min(total_distance_A, total_distance_B)

