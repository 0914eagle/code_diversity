
def min_panels_to_contain_defective_cells():
    n = int(input())
    coordinates = set()
    for _ in range(n):
        x, y, z = map(int, input().split())
        coordinates.add((x, y, z))

    panels = 6 * n
    for x, y, z in coordinates:
        if (x+1, y, z) not in coordinates:
            panels += 1
        if (x-1, y, z) not in coordinates:
            panels += 1
        if (x, y+1, z) not in coordinates:
            panels += 1
        if (x, y-1, z) not in coordinates:
            panels += 1
        if (x, y, z+1) not in coordinates:
            panels += 1
        if (x, y, z-1) not in coordinates:
            panels += 1

    print(panels)

min_panels_to_contain_defective_cells()
