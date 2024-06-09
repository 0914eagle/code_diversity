
def get_covered_length(buildings, D):
    # Sort the buildings by their height in descending order
    buildings.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the covered length to 0
    covered_length = 0
    
    # Iterate through the buildings and calculate the covered length
    for building in buildings:
        # If the building has a transmitter, add its height to the covered length
        if building[0] == 1:
            covered_length += building[1]
        # If the building does not have a transmitter, add the height of the previous building to the covered length
        else:
            covered_length += buildings[buildings.index(building) - 1][1]
    
    # Return the covered length
    return covered_length

