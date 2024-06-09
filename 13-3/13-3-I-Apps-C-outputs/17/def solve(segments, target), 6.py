
def solve(segments, target):
    # Initialize the position of the tip of the arm as the origin
    tip_position = [0, 0]
    
    # Loop through each segment and calculate the position of the tip
    for i in range(len(segments)):
        segment_length = segments[i]
        tip_position[0] += segment_length * math.cos(i * math.pi / 2)
        tip_position[1] += segment_length * math.sin(i * math.pi / 2)
    
    # Calculate the distance between the tip position and the target
    distance = math.sqrt((tip_position[0] - target[0]) ** 2 + (tip_position[1] - target[1]) ** 2)
    
    # Return the tip position and the distance
    return tip_position, distance

