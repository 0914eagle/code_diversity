
def get_box_heights(box_heights):
    # Sort the box heights in descending order
    sorted_box_heights = sorted(box_heights, reverse=True)

    # Get the tower heights
    tower_heights = sorted_box_heights[-2:]

    # Get the box heights for the first tower
    first_tower = sorted_box_heights[:3]

    # Get the box heights for the second tower
    second_tower = sorted_box_heights[3:]

    return first_tower, second_tower

