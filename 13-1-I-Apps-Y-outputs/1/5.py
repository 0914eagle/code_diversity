
def reconstruct_towers(box_heights):
    # Sort the box heights in non-decreasing order
    sorted_box_heights = sorted(box_heights)

    # Find the two tower heights
    tower_heights = sorted_box_heights[-2:]

    # Find the indices of the tower heights in the sorted box heights list
    tower_indices = [i for i, x in enumerate(sorted_box_heights) if x in tower_heights]

    # Create a list to store the tower box heights
    tower_box_heights = []

    # Loop through the tower indices and add the corresponding box heights to the tower list
    for i in range(len(tower_indices)):
        tower_box_heights.append(sorted_box_heights[tower_indices[i]])
        tower_box_heights.append(sorted_box_heights[tower_indices[i] + 1])
        tower_box_heights.append(sorted_box_heights[tower_indices[i] + 2])

    # Return the tower box heights in order of decreasing height
    return sorted(tower_box_heights, reverse=True)

