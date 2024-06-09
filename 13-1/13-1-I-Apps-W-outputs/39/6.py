
def get_minimum_distance(n, m, a, b, y, y_prime, l):
    # Initialize the minimum distance and the corresponding points
    min_distance = float('inf')
    point_a, point_b = 0, 0
    
    # Loop through all possible pairs of points
    for i in range(n):
        for j in range(m):
            # Calculate the distance between the two points
            distance = abs(y[i] - y_prime[j]) + l[j]
            
            # If the distance is less than the minimum distance, update the minimum distance and the corresponding points
            if distance < min_distance:
                min_distance = distance
                point_a = i + 1
                point_b = j + 1
    
    return point_a, point_b

