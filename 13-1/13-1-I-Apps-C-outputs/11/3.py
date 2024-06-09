
def max_area(n, m, k):
    # Initialize the maximum area to 0
    max_area = 0
    # Loop through all possible horizontal cuts
    for i in range(k+1):
        # Get the number of vertical cuts required for this horizontal cut
        num_vert_cuts = k - i
        # Check if the number of vertical cuts is valid
        if num_vert_cuts > 0 and num_vert_cuts <= k:
            # Calculate the area of the smallest piece
            area = (n // (i+1)) * (m // (num_vert_cuts+1))
            # Update the maximum area if necessary
            max_area = max(max_area, area)
    # Return the maximum area
    return max_area

