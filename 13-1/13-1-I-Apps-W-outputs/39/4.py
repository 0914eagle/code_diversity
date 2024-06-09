
def solve(n, m, a, b, y, y_prime, l):
    # Initialize the minimum distance and the points on the left and right banks
    min_dist = float('inf')
    left_point, right_point = 0, 0

    # Loop through all possible pairs of points on the left and right banks
    for i in range(n):
        for j in range(m):
            # Calculate the distance between the points
            dist = abs(a - b) + abs(y[i] - y_prime[j]) + l[j]

            # If the distance is less than the minimum distance, update the minimum distance and the points on the left and right banks
            if dist < min_dist:
                min_dist = dist
                left_point = i + 1
                right_point = j + 1

    # Return the points on the left and right banks
    return left_point, right_point

