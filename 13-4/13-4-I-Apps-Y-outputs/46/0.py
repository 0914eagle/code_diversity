
def get_tower_heights(box_heights):
    # Sort the box heights in decreasing order
    sorted_box_heights = sorted(box_heights, reverse=True)

    # The first tower height is the largest height in the input
    tower_1_height = sorted_box_heights[0]

    # The second tower height is the second largest height in the input
    tower_2_height = sorted_box_heights[1]

    # The tower heights are the first two elements of the sorted box heights
    tower_heights = [tower_1_height, tower_2_height]

    # The box heights are the remaining elements of the sorted box heights
    box_heights = sorted_box_heights[2:]

    # The boxes are ordered from largest to smallest
    box_heights.sort(reverse=True)

    return tower_heights, box_heights

