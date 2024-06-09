
def reconstruct_towers(box_heights):
    # Sort the box heights in non-decreasing order
    sorted_box_heights = sorted(box_heights)

    # Find the two tower heights
    tower_heights = sorted_box_heights[-2:]

    # Find the indices of the tower heights in the sorted box heights list
    tower_indices = [i for i, x in enumerate(sorted_box_heights) if x in tower_heights]

    # Find the indices of the boxes in the first tower
    first_tower_indices = tower_indices[0]

    # Find the indices of the boxes in the second tower
    second_tower_indices = tower_indices[1]

    # Create lists to store the heights of the boxes in each tower
    first_tower = []
    second_tower = []

    # Loop through the sorted box heights and add the heights to the appropriate tower list
    for i, height in enumerate(sorted_box_heights):
        if i in first_tower_indices:
            first_tower.append(height)
        elif i in second_tower_indices:
            second_tower.append(height)

    # Return the heights of the boxes in each tower in order of decreasing height
    return first_tower[::-1], second_tower[::-1]

