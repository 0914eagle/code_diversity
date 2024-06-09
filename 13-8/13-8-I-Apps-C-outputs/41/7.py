
def solve(N, L, positions):
    # Calculate the minimum distance between any two positions
    min_distance = 1 + 1e-9
    for i in range(N):
        for j in range(i+1, N):
            distance = abs(positions[i] - positions[j])
            if distance < min_distance:
                min_distance = distance
    
    # Calculate the maximum speed that will avoid collisions
    max_speed = (L - min_distance) / 2
    
    # Check if there is an optimal speed
    if max_speed >= 0.1 and max_speed <= 10:
        return max_speed
    else:
        return "no fika"

