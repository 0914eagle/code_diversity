
def solve(N, L, x):
    # Calculate the minimum distance between two luggage pieces
    min_distance = 1 + 1e-9
    
    # Initialize the maximum speed to be the minimum speed
    max_speed = 0.1
    
    # Iterate through each luggage piece
    for i in range(N):
        # Calculate the distance between the current luggage piece and the next luggage piece
        distance = abs(x[i] - x[(i+1)%N])
        
        # If the distance is less than the minimum distance, update the minimum distance
        if distance < min_distance:
            min_distance = distance
    
    # Calculate the maximum speed that will avoid all collisions
    max_speed = L / min_distance
    
    # Return the maximum speed
    return max_speed

