
def get_closest_position(segments, target):
    # Initialize the position of the tip of the arm
    position = [0, 0]
    
    # Loop through each segment and calculate the position of the tip
    for i in range(len(segments)):
        segment_length = segments[i]
        angle = i * 2 * math.pi / len(segments)
        x = segment_length * math.cos(angle)
        y = segment_length * math.sin(angle)
        position[0] += x
        position[1] += y
    
    # Calculate the distance between the target and the current position
    distance = math.sqrt((target[0] - position[0]) ** 2 + (target[1] - position[1]) ** 2)
    
    # Return the position of the tip and the distance to the target
    return position, distance

