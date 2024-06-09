
def solve(sticks):
    # Sort the sticks by their x-coordinate
    sticks.sort(key=lambda x: x[0])
    
    # Initialize the output list
    output = []
    
    # Loop through the sticks
    for stick in sticks:
        # Find the closest stick to the current stick
        closest_stick = None
        min_distance = float('inf')
        for other_stick in sticks:
            if other_stick != stick:
                distance = abs(stick[0] - other_stick[0])
                if distance < min_distance:
                    min_distance = distance
                    closest_stick = other_stick
        
        # Add the closest stick to the output list
        output.append(closest_stick)
    
    # Return the output list
    return output

