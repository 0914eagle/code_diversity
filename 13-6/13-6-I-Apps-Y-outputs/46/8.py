
def get_tower_heights(box_heights):
    # Find the two tower heights
    tower_heights = set(box_heights) - set(range(1, 101))
    assert len(tower_heights) == 2
    tower_heights = list(tower_heights)

    # Find the box heights for the first tower
    first_tower = []
    for box_height in box_heights:
        if box_height != tower_heights[0] and box_height != tower_heights[1]:
            first_tower.append(box_height)
    first_tower.sort(reverse=True)

    # Find the box heights for the second tower
    second_tower = []
    for box_height in box_heights:
        if box_height != first_tower[0] and box_height != first_tower[1] and box_height != first_tower[2]:
            second_tower.append(box_height)
    second_tower.sort(reverse=True)

    return first_tower + second_tower

def main():
    box_heights = [int(input()) for _ in range(8)]
    print(*get_tower_heights(box_heights))

if __name__ == '__main__':
    main()

