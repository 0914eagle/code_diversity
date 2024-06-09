
def max_area(n, m, k):
    # Initialize the maximum area to 0
    max_area = 0
    # Loop through all possible horizontal cuts
    for i in range(k+1):
        # Get the number of vertical cuts required for this horizontal cut
        v_cuts = k - i
        # Check if the number of vertical cuts is valid
        if v_cuts >= 0 and v_cuts <= k:
            # Calculate the area of the current combination
            area = (n // (i + 1)) * (m // (v_cuts + 1))
            # Update the maximum area if necessary
            max_area = max(max_area, area)
    # Return the maximum area
    return max_area

