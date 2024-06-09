
def get_tower_heights(box_heights):
    # Sort the box heights in descending order
    sorted_box_heights = sorted(box_heights, reverse=True)

    # Get the two tower heights
    tower_heights = sorted_box_heights[-2:]

    # Get the box heights for the first tower
    first_tower_box_heights = sorted_box_heights[:3]

    # Get the box heights for the second tower
    second_tower_box_heights = sorted_box_heights[3:6]

    return first_tower_box_heights, second_tower_box_heights

