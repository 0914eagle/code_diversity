
def solve(N, L, x):
    # Calculate the minimum distance between two luggage pieces
    min_dist = 1 + 1e-9
    
    # Initialize the maximum speed to a invalid value
    max_speed = -1
    
    # Iterate through all possible speeds
    for speed in range(10, 100):
        # Calculate the distance traveled by each luggage piece
        dist = [speed * i for i in range(N)]
        
        # Check if any two luggage pieces will collide
        for i in range(N):
            for j in range(i+1, N):
                if abs(dist[i] - dist[j]) < min_dist:
                    # If a collision is detected, break the loop
                    break
            else:
                # If no collision is detected, set the maximum speed to the current speed
                max_speed = speed
                break
    
    # Return the maximum speed
    return max_speed

