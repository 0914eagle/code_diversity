
def max_area(sticks):
    
    # Sort the sticks in non-decreasing order
    sticks.sort()
    # Initialize the maximum area to 0
    max_area = 0
    # Iterate through the sticks
    for i in range(len(sticks)):
        # Get the length of the current stick
        length = sticks[i]
        # Check if the length is at least 2
        if length >= 2:
            # Iterate through the remaining sticks
            for j in range(i+1, len(sticks)):
                # Get the length of the current stick
                width = sticks[j]
                # Check if the length is at most the half of the current length
                if width <= length // 2:
                    # Calculate the area of the rectangle
                    area = length * width
                    # Update the maximum area if necessary
                    max_area = max(max_area, area)
    # Return the maximum area
    return max_area

