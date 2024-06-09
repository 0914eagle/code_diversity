
def solve(segments, target):
    # Initialize the position of the tip of the robotic arm
    x, y = 0, 0
    
    # Iterate through each segment of the robotic arm
    for i in range(len(segments)):
        # Calculate the length of the current segment
        length = segments[i]
        
        # Calculate the angle between the current segment and the previous segment
        if i == 0:
            angle = 0
        else:
            angle = np.arctan2(y, x)
        
        # Calculate the position of the tip of the current segment
        x_new = x + length * np.cos(angle)
        y_new = y + length * np.sin(angle)
        
        # Update the position of the tip of the robotic arm
        x, y = x_new, y_new
    
    # Return the position of the tip of the robotic arm
    return x, y

