
def solve(n, lairs):
    # Sort the lairs by their x-coordinates
    lairs.sort(key=lambda x: x[0])

    # Initialize the minimum radius and center as infinity and (0, 0) respectively
    min_radius = float('inf')
    center = (0, 0)

    # Loop through each pair of lairs
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Calculate the distance between the two lairs
            distance = ((lairs[i][0] - lairs[j][0]) ** 2 + (lairs[i][1] - lairs[j][1]) ** 2) ** 0.5

            # If the distance is less than the minimum radius, update the minimum radius and center
            if distance < min_radius:
                min_radius = distance
                center = ((lairs[i][0] + lairs[j][0]) / 2, (lairs[i][1] + lairs[j][1]) / 2)

    # If the minimum radius is infinity, it is not possible to build a reserve
    if min_radius == float('inf'):
        return -1

    # Otherwise, return the minimum radius
    return min_radius

