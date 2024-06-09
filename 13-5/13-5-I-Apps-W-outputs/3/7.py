
def max_rectangle_area(sticks):
    # Sort the sticks by length in non-decreasing order
    sticks.sort()
    # Initialize the maximum area to 0
    max_area = 0
    # Loop through each stick and try to form rectangles with it
    for i in range(len(sticks)):
        for j in range(i, len(sticks)):
            # Check if the lengths of the two sticks form a valid rectangle
            if sticks[i] == sticks[j] and sticks[i] != 0:
                # Calculate the area of the rectangle
                area = sticks[i] * sticks[j]
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    return max_area

