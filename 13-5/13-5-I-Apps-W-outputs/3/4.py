
def get_max_area(sticks):
    
    # Sort the sticks in non-decreasing order
    sticks.sort()
    
    # Initialize the maximum total area
    max_area = 0
    
    # Iterate over the sticks
    for i in range(len(sticks)):
        for j in range(i, len(sticks)):
            # Check if the sticks form a valid rectangle
            if sticks[i] == sticks[j] and sticks[i] != sticks[j-1]:
                # Calculate the area of the rectangle
                area = sticks[i] * (j - i + 1)
                
                # Update the maximum total area
                max_area = max(max_area, area)
    
    return max_area

