
def get_max_area(sticks):
    # Sort the sticks in non-decreasing order
    sticks.sort()
    # Initialize the maximum area and the current area
    max_area = 0
    current_area = 0
    # Iterate through the sticks
    for i in range(len(sticks)):
        # Check if the current stick is equal to the previous stick
        if i > 0 and sticks[i] == sticks[i-1]:
            # If they are equal, calculate the area of the current rectangle
            current_area = sticks[i] * (i+1)
        # If the current stick is not equal to the previous stick, calculate the area of the current rectangle
        else:
            current_area = sticks[i] * (i+1)
        # Update the maximum area if the current area is greater than the maximum area
        if current_area > max_area:
            max_area = current_area
    return max_area

