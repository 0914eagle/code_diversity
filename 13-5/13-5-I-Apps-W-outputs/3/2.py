
def max_rectangle_area(sticks):
    
    # Sort the sticks in non-decreasing order
    sticks.sort()
    # Initialize the maximum area to 0
    max_area = 0
    # Iterate over the sticks
    for i in range(len(sticks)):
        # Get the length of the current stick
        length = sticks[i]
        # Iterate over the remaining sticks
        for j in range(i+1, len(sticks)):
            # Get the length of the next stick
            next_length = sticks[j]
            # Check if the current stick is equal to the next stick
            if length == next_length:
                # If they are equal, calculate the area of the rectangle
                area = length * next_length
                # Update the maximum area if necessary
                max_area = max(max_area, area)
            # Check if the current stick is less than the next stick
            elif length < next_length:
                # If it is, calculate the area of the rectangle
                area = length * next_length
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    # Return the maximum area
    return max_area

