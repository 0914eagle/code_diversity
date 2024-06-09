
def max_rectangle_area(sticks):
    
    # Sort the sticks in non-decreasing order
    sticks.sort()
    # Initialize the maximum area to 0
    max_area = 0
    # Loop through each stick and consider it as the first side of the rectangle
    for i in range(len(sticks)):
        # Consider the second side of the rectangle as the next stick in the list
        for j in range(i+1, len(sticks)):
            # Check if the first and second sides form a valid rectangle
            if sticks[i] <= sticks[j]:
                # Calculate the area of the rectangle
                area = sticks[i] * sticks[j]
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    return max_area

