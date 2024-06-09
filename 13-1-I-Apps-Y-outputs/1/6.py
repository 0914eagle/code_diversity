
def reconstruct_art_exhibit(box_heights):
    # Sort the box heights in non-decreasing order
    sorted_box_heights = sorted(box_heights)

    # Find the two tower heights
    tower_heights = sorted_box_heights[-2:]

    # Find the indices of the boxes in the first tower
    first_tower_indices = [i for i, h in enumerate(sorted_box_heights) if h == tower_heights[0]]

    # Find the indices of the boxes in the second tower
    second_tower_indices = [i for i, h in enumerate(sorted_box_heights) if h == tower_heights[1]]

    # Reconstruct the first tower
    first_tower = [sorted_box_heights[i] for i in first_tower_indices]

    # Reconstruct the second tower
    second_tower = [sorted_box_heights[i] for i in second_tower_indices]

    return first_tower, second_tower

