
def get_box_heights(box_heights):
    # Sort the box heights in non-decreasing order
    sorted_box_heights = sorted(box_heights)

    # Find the two tower heights
    tower_heights = [sorted_box_heights[-1], sorted_box_heights[-2]]

    # Find the three boxes in the first tower
    first_tower = [tower_heights[0]]
    for box in sorted_box_heights:
        if box < tower_heights[0]:
            first_tower.append(box)
        else:
            break

    # Find the three boxes in the second tower
    second_tower = [tower_heights[1]]
    for box in sorted_box_heights:
        if box < tower_heights[1]:
            second_tower.append(box)
        else:
            break

    return first_tower, second_tower

