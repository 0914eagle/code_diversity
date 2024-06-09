
def get_closest_configuration(segments, target):
    # Initialize the configuration of the robotic arm
    configuration = [0] * len(segments)

    # Iterate through each segment of the robotic arm
    for i in range(len(segments)):
        # Compute the distance between the target point and the current segment
        distance = get_distance(target, configuration[i])

        # If the distance is less than the minimum distance, update the minimum distance and the corresponding segment index
        if distance < min_distance:
            min_distance = distance
            min_index = i

    # Update the configuration of the robotic arm with the minimum distance and segment index
    configuration[min_index] = target

    return configuration

def get_distance(point1, point2):
    # Compute the Euclidean distance between the two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

