
def min_panels_to_contain_defective_cells():
    n = int(input())
    defective_cells = set()
    for _ in range(n):
        x, y, z = map(int, input().split())
        defective_cells.add((x, y, z))

    panels = 6 * n
    for x, y, z in defective_cells:
        if (x+1, y, z) not in defective_cells:
            panels += 1
        if (x-1, y, z) not in defective_cells:
            panels += 1
        if (x, y+1, z) not in defective_cells:
            panels += 1
        if (x, y-1, z) not in defective_cells:
            panels += 1
        if (x, y, z+1) not in defective_cells:
            panels += 1
        if (x, y, z-1) not in defective_cells:
            panels += 1

    print(panels)

min_panels_to_contain_defective_cells()
