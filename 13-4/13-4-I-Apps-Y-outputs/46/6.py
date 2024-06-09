
def reconstruct_towers(box_heights):
    # Sort the box heights in descending order
    sorted_box_heights = sorted(box_heights, reverse=True)

    # Find the two tower heights
    tower_heights = sorted_box_heights[-2:]

    # Find the three boxes in the first tower
    first_tower = sorted_box_heights[:3]

    # Find the three boxes in the second tower
    second_tower = sorted_box_heights[3:6]

    return first_tower, second_tower

