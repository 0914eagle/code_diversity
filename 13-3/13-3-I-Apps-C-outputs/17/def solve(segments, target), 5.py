
def solve(segments, target):
    # Initialize the position of the tip of the robotic arm as (0, 0)
    tip_position = (0, 0)
    
    # Iterate through each segment of the robotic arm
    for i in range(len(segments)):
        # Calculate the position of the tip of the current segment
        segment_position = (tip_position[0] + segments[i], tip_position[1])
        
        # Update the position of the tip of the robotic arm to the position of the current segment
        tip_position = segment_position
    
    # Calculate the distance between the tip of the robotic arm and the target
    distance = ((tip_position[0] - target[0]) ** 2 + (tip_position[1] - target[1]) ** 2) ** 0.5
    
    # Return the position of the tip of the robotic arm and the distance to the target
    return tip_position, distance

