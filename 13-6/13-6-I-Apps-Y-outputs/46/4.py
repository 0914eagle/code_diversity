
def get_sorted_box_heights(box_heights):
    # Sort the box heights in decreasing order
    sorted_box_heights = sorted(box_heights, reverse=True)
    return sorted_box_heights

def get_tower_heights(box_heights, tower_heights):
    # Get the indices of the boxes that belong to the first tower
    first_tower_indices = [i for i, h in enumerate(box_heights) if h == tower_heights[0]]

    # Get the indices of the boxes that belong to the second tower
    second_tower_indices = [i for i, h in enumerate(box_heights) if h == tower_heights[1]]

    # Get the heights of the boxes that belong to the first tower
    first_tower_heights = [box_heights[i] for i in first_tower_indices]

    # Get the heights of the boxes that belong to the second tower
    second_tower_heights = [box_heights[i] for i in second_tower_indices]

    return first_tower_heights, second_tower_heights

def main():
    box_heights = [12, 8, 2, 4, 10, 3, 25, 14]
    tower_heights = [25, 14]
    sorted_box_heights = get_sorted_box_heights(box_heights)
    first_tower_heights, second_tower_heights = get_tower_heights(sorted_box_heights, tower_heights)
    print(first_tower_heights)
    print(second_tower_heights)

if __name__ == '__main__':
    main()

