
def get_covered_length(buildings, D):
    # Sort the buildings by their height in descending order
    buildings.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the covered length as 0
    covered_length = 0
    
    # Iterate through the buildings and calculate the covered length
    for building in buildings:
        # If the building has a transmitter, add its height to the covered length
        if building[0] == 1:
            covered_length += building[1]
        # If the building does not have a transmitter, check if it blocks the signal from the previous building
        else:
            # If the previous building is taller than the current building, add the height of the previous building to the covered length
            if buildings[0][1] > building[1]:
                covered_length += buildings[0][1]
            # If the previous building is not taller than the current building, add the height of the current building to the covered length
            else:
                covered_length += building[1]
    
    # Return the covered length
    return covered_length

