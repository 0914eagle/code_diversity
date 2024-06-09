
def solve(heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    
    # Initialize variables to keep track of the minimum number of buns needed and the step of the progression
    min_buns = 0
    step = 0
    
    # Loop through the heights and calculate the minimum number of buns needed to make the progression non-decreasing
    for i in range(len(heights) - 1):
        # Calculate the difference between the current height and the next height
        diff = heights[i + 1] - heights[i]
        
        # If the difference is negative, it means the progression is not non-decreasing yet
        if diff < 0:
            # Calculate the number of buns needed to make the progression non-decreasing
            buns_needed = abs(diff)
            
            # Update the minimum number of buns needed if necessary
            if buns_needed > min_buns:
                min_buns = buns_needed
                step = diff
    
    # Return the minimum number of buns needed and the step of the progression
    return min_buns, step

