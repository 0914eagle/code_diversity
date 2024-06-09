
def get_tower_heights(box_heights):
    # Sort the box heights in non-decreasing order
    sorted_box_heights = sorted(box_heights)

    # Find the two tower heights
    tower_heights = [sorted_box_heights[-1], sorted_box_heights[-2]]

    # Find the three boxes in the first tower
    first_tower = [box for box in sorted_box_heights if box != tower_heights[0] and box != tower_heights[1]]

    # Find the three boxes in the second tower
    second_tower = [box for box in sorted_box_heights if box != first_tower[0] and box != first_tower[1] and box != first_tower[2]]

    return first_tower + second_tower

