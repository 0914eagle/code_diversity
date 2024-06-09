
def get_closest_configuration(segments, target):
    # Initialize the configuration as the origin
    configuration = [0, 0] * len(segments)

    # Iterate through each segment
    for i in range(len(segments)):
        # Calculate the distance from the target to the segment's endpoint
        distance = get_distance(configuration[i], target)

        # If the distance is less than the minimum distance, update the minimum distance and the configuration
        if distance < min_distance:
            min_distance = distance
            closest_configuration = configuration[:]

    return closest_configuration

def get_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

