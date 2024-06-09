
def get_closest_configuration(segments, target):
    # Initialize the configuration as the origin
    configuration = [0, 0] * len(segments)

    # Loop through each segment and calculate the closest point on the segment to the target
    for i in range(len(segments)):
        segment_length = segments[i]
        segment_angle = 2 * i * math.pi / len(segments)
        segment_x = segment_length * math.cos(segment_angle)
        segment_y = segment_length * math.sin(segment_angle)
        configuration[i] = [segment_x, segment_y]

    # Return the closest configuration to the target
    return configuration

