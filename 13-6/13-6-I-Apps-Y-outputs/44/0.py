
def count_inns_with_ocean_view(heights):
    # Initialize a variable to store the number of inns with ocean view
    inns_with_ocean_view = 0

    # Iterate through the list of heights
    for i in range(len(heights)):
        # Check if the current inn is visible from the ocean
        if all(heights[j] <= heights[i] for j in range(i)):
            # If visible, increment the number of inns with ocean view
            inns_with_ocean_view += 1

    # Return the number of inns with ocean view
    return inns_with_ocean_view

