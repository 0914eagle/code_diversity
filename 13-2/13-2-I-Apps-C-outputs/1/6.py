
def get_min_distance(shadow_walk, lydia_walk):
    # Calculate the distance between the starting points of Shadow and Lydia
    start_dist = get_distance(shadow_walk[0], lydia_walk[0])

    # Initialize the minimum distance between Shadow and Lydia
    min_dist = start_dist

    # Loop through each point in Shadow's walk
    for i in range(1, len(shadow_walk)):
        # Calculate the distance between the current point and Lydia's starting point
        curr_dist = get_distance(shadow_walk[i], lydia_walk[0])

        # Update the minimum distance if necessary
        min_dist = min(min_dist, curr_dist)

    # Loop through each point in Lydia's walk
    for i in range(1, len(lydia_walk)):
        # Calculate the distance between the current point and Shadow's starting point
        curr_dist = get_distance(lydia_walk[i], shadow_walk[0])

        # Update the minimum distance if necessary
        min_dist = min(min_dist, curr_dist)

    return min_dist

def get_distance(point1, point2):
    # Calculate the Euclidean distance between the two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

shadow_walk = [(0, 0), (10, 0)]
lydia_walk = [(30, 0), (15, 0)]
print(get_min_distance(shadow_walk, lydia_walk))

