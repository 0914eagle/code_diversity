
def get_max_buns(heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the maximum number of buns eaten by one student to 0
    max_buns = 0
    # Initialize the step of the resulting progression to 0
    step = 0
    # Loop through the heights and find the maximum number of buns eaten by one student
    for i in range(len(heights) - 1):
        # Calculate the difference between the current height and the next height
        diff = heights[i + 1] - heights[i]
        # If the difference is positive, it means that the next height is greater than the current height, so we can give a bun of the first type to the current student
        if diff > 0:
            max_buns += 1
        # If the difference is negative, it means that the next height is less than the current height, so we can give a bun of the second type to the current student
        elif diff < 0:
            max_buns += 1
        # Update the step of the resulting progression
        step = diff
    # Return the maximum number of buns eaten by one student and the step of the resulting progression
    return max_buns, step

