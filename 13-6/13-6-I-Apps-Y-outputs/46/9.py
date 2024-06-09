
def get_box_heights(box_heights):
    # Sort the box heights in decreasing order
    sorted_box_heights = sorted(box_heights, reverse=True)
    # Get the two tower heights
    tower_heights = sorted_box_heights[-2:]
    # Get the three boxes in the first tower
    first_tower = sorted_box_heights[:3]
    # Get the three boxes in the second tower
    second_tower = sorted_box_heights[3:6]
    return first_tower, second_tower

def main():
    box_heights = [12, 8, 2, 4, 10, 3, 25, 14]
    first_tower, second_tower = get_box_heights(box_heights)
    print(first_tower)
    print(second_tower)

if __name__ == '__main__':
    main()

