
def get_box_heights(box_heights):
    # Sort the box heights in decreasing order
    sorted_box_heights = sorted(box_heights, reverse=True)
    # The first tower height is the largest height in the input
    first_tower_height = sorted_box_heights[0]
    # The second tower height is the second largest height in the input
    second_tower_height = sorted_box_heights[1]
    # The heights of the three boxes in the first tower are the largest three heights
    first_tower_box_heights = sorted_box_heights[:3]
    # The heights of the three boxes in the second tower are the smallest three heights
    second_tower_box_heights = sorted_box_heights[3:]
    return first_tower_box_heights, second_tower_box_heights

def main():
    box_heights = [int(input()) for _ in range(6)]
    first_tower_box_heights, second_tower_box_heights = get_box_heights(box_heights)
    print(*first_tower_box_heights, sep=' ')
    print(*second_tower_box_heights, sep=' ')

if __name__ == '__main__':
    main()

