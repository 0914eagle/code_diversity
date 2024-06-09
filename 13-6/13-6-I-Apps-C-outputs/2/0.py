
def f1(n, m):
    # function to check if the gargoyle can be rotated
    def can_rotate(gargoyle, gargoyle_list):
        for g in gargoyle_list:
            if g[0] == gargoyle[1] and g[1] == gargoyle[0]:
                return True
        return False

    # function to rotate the gargoyle
    def rotate(gargoyle):
        if gargoyle[0] == "V":
            return ("H", gargoyle[1])
        else:
            return ("V", gargoyle[1])

    # function to find the minimum number of gargoyles that have to be rotated
    def find_min_rotations(gargoyle_list):
        min_rotations = 0
        for g in gargoyle_list:
            if can_rotate(g, gargoyle_list):
                min_rotations += 1
        return min_rotations

    # read the floorplan of the tomb
    floorplan = []
    for i in range(n):
        line = input()
        floorplan.append(line)

    # find the gargoyles in the floorplan
    gargoyles = []
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] in ["V", "H"]:
                gargoyles.append((floorplan[i][j], (i, j)))

    # find the minimum number of gargoyles that have to be rotated
    min_rotations = find_min_rotations(gargoyles)

    # return the minimum number of gargoyles that have to be rotated
    return min_rotations

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

