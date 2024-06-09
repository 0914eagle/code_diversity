
def solve(segments, target):
    # Calculate the distance between the target and the origin
    distance = ((target[0]) ** 2 + (target[1]) ** 2) ** 0.5

    # Initialize the position of the tip of the robotic arm
    x = 0
    y = 0

    # Loop through each segment and calculate the position of the tip
    for i in range(len(segments)):
        segment_length = segments[i]
        angle = (i * 2 * math.pi) / len(segments)
        x_new = x + segment_length * math.cos(angle)
        y_new = y + segment_length * math.sin(angle)
        x = x_new
        y = y_new

    # Calculate the distance between the tip of the robotic arm and the target
    distance_new = ((x - target[0]) ** 2 + (y - target[1]) ** 2) ** 0.5

    # Return the position of the tip of the robotic arm
    return [x, y]

