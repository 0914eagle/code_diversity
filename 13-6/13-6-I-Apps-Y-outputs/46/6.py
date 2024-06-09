
def get_tower_heights(box_heights):
    tower_heights = []
    for i in range(2):
        tower_heights.append(box_heights.pop())
    return tower_heights

def get_box_heights(box_heights, tower_heights):
    box_heights.sort(reverse=True)
    tower_1_heights = []
    tower_2_heights = []
    for i in range(3):
        tower_1_heights.append(box_heights.pop())
    for i in range(3):
        tower_2_heights.append(box_heights.pop())
    return tower_1_heights, tower_2_heights

def main():
    box_heights = [12, 8, 2, 4, 10, 3, 25, 14]
    tower_heights = get_tower_heights(box_heights)
    tower_1_heights, tower_2_heights = get_box_heights(box_heights, tower_heights)
    print(tower_1_heights)
    print(tower_2_heights)

if __name__ == '__main__':
    main()

