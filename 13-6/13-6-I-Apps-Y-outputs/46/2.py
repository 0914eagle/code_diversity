
def get_sorted_boxes(box_heights):
    # Sort the box heights in descending order
    sorted_box_heights = sorted(box_heights, reverse=True)
    # Get the two tower heights
    tower_heights = sorted_box_heights[-2:]
    # Get the three boxes in the first tower
    first_tower = sorted_box_heights[:3]
    # Get the three boxes in the second tower
    second_tower = sorted_box_heights[3:6]
    # Return the sorted boxes
    return first_tower, second_tower

def main():
    # Test case 1
    box_heights = [12, 8, 2, 4, 10, 3, 25, 14]
    first_tower, second_tower = get_sorted_boxes(box_heights)
    print(first_tower)
    print(second_tower)

    # Test case 2
    box_heights = [14, 10, 8, 4, 3, 2, 25, 12]
    first_tower, second_tower = get_sorted_boxes(box_heights)
    print(first_tower)
    print(second_tower)

if __name__ == '__main__':
    main()

