
def get_closest_configuration(segments, target):
    # Initialize the configuration as the origin
    configuration = [0] * len(segments)

    # Iterate through each segment and calculate the angle and length
    for i in range(len(segments)):
        segment_length = segments[i]
        segment_angle = 2 * i * math.pi / len(segments)
        configuration[i] = (segment_length * math.cos(segment_angle), segment_length * math.sin(segment_angle))

    # Calculate the distance between the target and the configuration
    distance = math.sqrt((target[0] - configuration[0][0]) ** 2 + (target[1] - configuration[0][1]) ** 2)

    # If the distance is within the tolerance, return the configuration
    if distance <= 0.01:
        return configuration

    # Otherwise, find the closest configuration by iterating through each segment and adjusting the angle and length
    for i in range(len(segments)):
        segment_length = segments[i]
        segment_angle = 2 * i * math.pi / len(segments)
        configuration[i] = (segment_length * math.cos(segment_angle), segment_length * math.sin(segment_angle))
        distance = math.sqrt((target[0] - configuration[0][0]) ** 2 + (target[1] - configuration[0][1]) ** 2)
        if distance <= 0.01:
            return configuration

    # If no configuration is found, return None
    return None

