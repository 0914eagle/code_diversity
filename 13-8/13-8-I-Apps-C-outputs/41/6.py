
def solve(N, L, x):
    # Calculate the maximum speed such that no collisions occur
    max_speed = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(x[i] - x[j]) <= 1:
                max_speed = max(max_speed, abs(x[i] - x[j]) / L)
    return max_speed

