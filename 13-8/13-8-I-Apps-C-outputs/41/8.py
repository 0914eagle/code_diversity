
def solve(N, L, positions):
    # Calculate the minimum distance between two pieces of luggage
    min_distance = 1 + 1e-9
    
    # Initialize the maximum speed to 0
    max_speed = 0
    
    # Iterate through each pair of positions
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the distance between the two positions
            distance = abs(positions[i] - positions[j])
            
            # If the distance is less than the minimum distance, update the minimum distance and maximum speed
            if distance < min_distance:
                min_distance = distance
                max_speed = (L - min_distance) / min_distance
    
    # Return the maximum speed
    return max_speed

