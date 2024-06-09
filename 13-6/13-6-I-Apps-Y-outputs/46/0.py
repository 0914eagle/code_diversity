
def get_box_heights(box_heights):
    # Sort the box heights in descending order
    sorted_box_heights = sorted(box_heights, reverse=True)
    # Find the two tower heights
    tower_heights = [sorted_box_heights[0], sorted_box_heights[-1]]
    # Find the three boxes in the first tower
    first_tower = [sorted_box_heights[0], sorted_box_heights[1], sorted_box_heights[2]]
    # Find the three boxes in the second tower
    second_tower = [sorted_box_heights[3], sorted_box_heights[4], sorted_box_heights[5]]
    return first_tower, second_tower

def main():
    box_heights = [12, 8, 2, 4, 10, 3, 25, 14]
    first_tower, second_tower = get_box_heights(box_heights)
    print(first_tower)
    print(second_tower)

if __name__ == '__main__':
    main()

