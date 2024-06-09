
def solve(heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the number of buns eaten by each student to 0
    buns_eaten = [0] * len(heights)
    # Initialize the maximum number of buns eaten by one student to 0
    max_buns = 0
    # Initialize the step of the progression to 0
    step = 0
    # Loop through the heights and calculate the number of buns needed to make them non-decreasing
    for i in range(len(heights) - 1):
        # Calculate the difference between the current height and the next height
        diff = heights[i + 1] - heights[i]
        # If the difference is positive, give two buns of the first type to the current student
        if diff > 0:
            buns_eaten[i] += 2
        # If the difference is negative, give one bun of the second type to the current student
        elif diff < 0:
            buns_eaten[i] += 1
        # Update the maximum number of buns eaten by one student
        max_buns = max(max_buns, buns_eaten[i])
        # Update the step of the progression
        step = heights[i + 1] - heights[i]
    # Return the maximum number of buns eaten by one student and the step of the progression
    return max_buns, step

